
import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer

#BLYNK_AUTH_TOKEN = 'yourapi'

device1 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(device1, GPIO.OUT)
GPIO.output(device1, GPIO.LOW)


# Initialize Blynk
blynk = BlynkLib.Blynk('Ow8ZniSxtawmAw63VRSsGIde7uUFpF6T')

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device1, GPIO.HIGH)
        print('Device1 HIGH')
    else:
        GPIO.output(device1, GPIO.LOW)
        print('Device1 LOW')


#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Alert: Hi! Raspberry Pi Connected to New Blynk2.0") 

while True:
    blynk.run()
