import os, sys, time
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from edge_impulse_linux.image import ImageImpulseRunner
import bluetooth

# Settings
# sudo chgrp bluetooth /var/run/sdp
service_uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
res_width = 480 #96
res_height = 480 #96

# BT Connection
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

with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (res_width, res_height)
    raw_capture = PiRGBArray(camera, size=(res_width, res_height))
    for frame in camera.capture_continuous(raw_capture, format= 'bgr', use_video_port=True):
        img = frame.array

        cv2.imshow("Mat Training", img)
        #client_sock.send(img)
        #client_sock.send(str.encode("\n"))
        raw_capture.truncate(0)
        if cv2.waitKey(1) == ord('q'):
            break

client_sock.close()
server_sock.close()
cv2.destroyAllWindows()
print("All done.")