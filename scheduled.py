import os
import schedule
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendFirstCommitment(slack_client, msg1):
  # make the POST request through the python slack client
  
  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#test',
      text=msg1
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)


def sendSecondCommitment(slack_client, msg2):
  # make the POST request through the python slack client
  
  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#test',
      text=msg2
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)



if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['REMINDER_SLACK_TOKEN']
## This token is stored in the ~/.zshrc file in the top-level directory
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  msg1 = "*Daily Conscious Leadership commitment reminder: Responsibility.* I commit to taking full responsibility for the circumstances of my life, and my physical, emotional, mental and spiritual wellbeing. I commit to support others to take full responsibility for their lives."
  msg2 = "*Daily Conscious Leadership commitment reminder: Curiosity.* I commit to growing in self-awareness. I commit to regarding every interaction as an opportunity to learn. I commit to curiosity as a path to rapid learning."

  schedule.every(5).seconds.do(lambda: sendSecondCommitment(slack_client, msg1))
  time.sleep(3)
  schedule.every(5).seconds.do(lambda: sendSecondCommitment(slack_client, msg2))


  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(1) # sleep for 1 second between checks




