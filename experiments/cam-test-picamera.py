from time import sleep
from picamera import PiCamera
#from PIL import Image

camera = PiCamera()
camera.resolution = (1024, 768)

camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('camera.jpg')

#image = Image.open('camera.jpg')
#image.show()
