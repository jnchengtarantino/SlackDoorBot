import os
from slack import RTMClient
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pwm = GPIO.PWM(13, 50)
pwm.start(0)

@RTMClient.run_on(event="message")
def onMessage(**payload):
  print(payload)
  pwm.ChangeDutyCycle(50)
  sleep(1)
  pwm.ChangeDutyCycle(0)
  
slack_token = os.environ["SLACK_BOT_TOKEN"]
rtm_client = RTMClient(token=slack_token)
rtm_client.start()