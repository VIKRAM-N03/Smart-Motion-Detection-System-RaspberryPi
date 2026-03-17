import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from datetime import datetime
from email_alert import send_email

PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

camera = PiCamera()

def capture_image():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"images/motion_{timestamp}.jpg"
    camera.capture(file_path)
    print("Image saved:", file_path)
    return file_path

print("System Ready...")
time.sleep(5)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")

            image = capture_image()
            send_email(image)

            time.sleep(10)

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()