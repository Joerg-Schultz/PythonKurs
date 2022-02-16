import os, sys, time
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from edge_impulse_linux.image import ImageImpulseRunner
import bluetooth

# Settings
# sudo chgrp bluetooth /var/run/sdp
service_uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
model_file = "modelfile.eim"
res_width = 480 #96
res_height = 480 #96
cutoff = 0.90
smoothing = 2 # how many frames have to be changed before a change is reported
draw_fps = True
write_video = True

# Load Model File
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, model_file)
runner = ImageImpulseRunner(model_path)

try:
    model_info = runner.init()
    print("Model Name: ", model_info['project']['name'])
    print("Model Owner: ", model_info['project']['owner'])
except Exception as e:
    print("ERROR: Could not initialise model")
    print("Exception: ", e)
    if runner:
        runner.stop()
    sys.exit(1)

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

bluetooth.advertise_service(server_sock, "SampleServer", service_id=service_uuid,
                            service_classes=[service_uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

if write_video :
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('BT_VisionMat.avi', fourcc, 19, (res_width, res_height))

smooth_array = []
fps = 0
with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (res_width, res_height)
    raw_capture = PiRGBArray(camera, size=(res_width, res_height))
    for frame in camera.capture_continuous(raw_capture, format= 'bgr', use_video_port=True):
        timestamp = cv2.getTickCount()  # calc framerate
        img = frame.array
        features, cropped = runner.get_features_from_image(img)
        try:
            res = runner.classify(features)
        except Exception as e:
            print("Could not perform inference")
            print("Exception: ", e)

        # Evalute ML
        background = res['result']['classification']['background']
        dog_on_mat = res['result']['classification']['dogonmat']
        print("Background: ", background, "Dog: ", dog_on_mat)
        current_status = False
        if dog_on_mat >= cutoff:
            current_status = True
        print("Status: ", current_status)

        # #Send status updates to BT
        # if current_status != dog_status :
        #     message = "Start" if current_status else "Stop"
        #     client_sock.send(str.encode(message))
        #     client_sock.send(str.encode("\n"))
        #     dog_status = current_status

        # # Send status continuously
        # message = "Start" if current_status else "Stop"
        # client_sock.send(str.encode(message))
        # client_sock.send(str.encode("\n"))

        # Send smoothed status
        if len(smooth_array) == smoothing: smooth_array.pop(0)
        smooth_array.append(current_status)
        if all(smooth_array): client_sock.send(str.encode("Start\n")) # all elements are true
        if not any(smooth_array): client_sock.send(str.encode("Stop\n"))# any will return True if there's any truth value in the iterable

        # Show Video
        # with classification result
        notification = "On Mat" if current_status else "No Dog"
        color = (0, 255, 0) if current_status else (255, 0, 0)
        cv2.putText(img, notification, (0, 70), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)
        #and fps
        if draw_fps:
            cv2.putText(img, "FPS: " + str(round(fps, 2)), (300, 12), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
        cv2.imshow("Mat Training", img)

        if write_video:
            out.write(img)


        raw_capture.truncate(0)

        # Calculate framrate
        frame_time = (cv2.getTickCount() - timestamp) / cv2.getTickFrequency()
        fps = 1 / frame_time
        if cv2.waitKey(1) == ord('q'):
            break

client_sock.close()
server_sock.close()
if write_video:
    out.release()
cv2.destroyAllWindows()
print("All done.")