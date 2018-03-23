import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,1)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22,1)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27,1)

def light_led(code):
  print(code)
  if(len(code) == 3):
    GPIO.output(17, int(code[0]))
    GPIO.output(22, int(code[1]))
    GPIO.output(27, int(code[2]))
  else:
    print("sorry color not supported.", color)

def color_to_code(color):
  if color == "red":
    return "010"
  elif color == "green":
    return "001"
  elif color == "blue":
    return "100"
  elif color == "yellow":
    return "011"
  elif color == "off":
    return "000"
  else:
    return "000"

try:
  while(True):
    request = raw_input("Enter color-> ")
    print(request)
    light_led(color_to_code(request))

except KeyboardInterrupt:
    GPIO.cleanup()
