import os, sys, time
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from edge_impulse_linux.image import ImageImpulseRunner

# Settings
model_file = "modelfile.eim"
res_width = 480 #96
res_height = 480 #96
cutoff = 0.85

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

#framerate
fps = 0
with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (res_width, res_height)
    raw_capture = PiRGBArray(camera, size=(res_width, res_height))
    for frame in camera.capture_continuous(raw_capture, format= 'bgr', use_video_port=True):
        img = frame.array
        features, cropped = runner.get_features_from_image(img)
        try:
            res = runner.classify(features)
        except Exception as e:
            print("Could not perform inference")
            print("Exception: ", e)
        #print("Output :", res)

        background = res['result']['classification']['background']
        dog_on_mat = res['result']['classification']['dogonmat']
        print("Background: ", background, "Dog: ", dog_on_mat)

        current_status = False
        if dog_on_mat >= cutoff:
            current_status = True
        notification = "On Mat" if current_status else "No Dog"
        color = (0, 255, 0) if current_status else (255, 0, 0)
        cv2.putText(img, notification, (0, 70), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        cv2.imshow("Dog on Mat", img)

        raw_capture.truncate(0)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
