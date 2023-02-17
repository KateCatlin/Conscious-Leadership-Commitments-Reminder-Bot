import os
import schedule
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  
  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#test',
      text=msg
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['REMINDER_SLACK_TOKEN']
## This token is stored in the ~/.zshrc file in the top-level directory
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  msg = "*Daily Conscious Leadership commitment reminder: Responsibility*. I commit to taking full responsibility for the circumstances of my life, and my physical, emotional, mental and spiritual wellbeing. I commit to support others to take full responsibility for their lives."
  schedule.every(15).seconds.do(lambda: sendMessage(slack_client, msg))

  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(1) # sleep for 1 second between checks
