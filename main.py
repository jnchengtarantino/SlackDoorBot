import os
from slack import RTMClient
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)
pwm.start(0)

@RTMClient.run_on(event="message")
def onMessage(**payload):
    print(payload)
#   pwm.ChangeDutyCycle(50)
#   sleep(1)
#   pwm.ChangeDutyCycle(0)
    data = payload['data']
    web_client = payload['web_client']

    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user'] # This is not username but user ID (the format is either U*** or W***)

    web_client.chat_postMessage(
        channel=channel_id,
        text=f"Hi <@{user}>!",
        thread_ts=thread_ts
    )
  
slack_token = os.environ["SLACK_BOT_TOKEN"]
rtm_client = RTMClient(token=slack_token)
rtm_client.start()