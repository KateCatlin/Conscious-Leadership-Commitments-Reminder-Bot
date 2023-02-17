import os
import schedule
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendCommitment(slack_client, commitment):
  # make the POST request through the python slack client
  
  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#test',
      text=commitment
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)


if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['REMINDER_SLACK_TOKEN']
## This token is stored in the ~/.zshrc file in the top-level directory
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  commitment1 = "*Daily Conscious Leadership commitment reminder: Responsibility.* I commit to taking full responsibility for the circumstances of my life, and my physical, emotional, mental and spiritual wellbeing. I commit to support others to take full responsibility for their lives."
  commitment2 = "*Daily Conscious Leadership commitment reminder: Curiosity.* I commit to growing in self-awareness. I commit to regarding every interaction as an opportunity to learn. I commit to curiosity as a path to rapid learning."
  commitment3 = "*Daily Conscious Leadership commitment reminder: Feelings.* I commit to feeling my feelings all the way through to completion. They come, and I locate them in my body then move, breathe and vocalize them so they release all the way through."
  commitment4 = "*Daily Conscious Leadership commitment reminder: Candor.* I commit to saying what is true for me. I commit to being a person to whom others can express themselves with candor."
  commitment5 = "*Daily Conscious Leadership commitment reminder: Gossip.* I commit to ending gossip, talking directly to people with whom I have an issue or concern, and encouraging others to talk directly to people with whom they have an issue or concern."
  commitment6 = "*Daily Conscious Leadership commitment reminder: Integrity.* I commit to the masterful practice of integrity, including acknowledging all authentic feelings, expressing the unarguable truth and keeping my agreements."
  commitment7 = "*Daily Conscious Leadership commitment reminder: Appreciation.* I commit to living in appreciation, fully opening to both receiving and giving appreciation."  
  commitment8 = "*Daily Conscious Leadership commitment reminder: Genius.* I commit to expressing my full magnificence, and to supporting and inspiring others to fully express their creativity and live in their zone of genius."
  commitment9 = "*Daily Conscious Leadership commitment reminder: Play and Rest.* I commit to creating a life of play, improvisation, and laughter. I commit to seeing all of life unfold easefully and effortlessly. I commit to maximizing my energy by honoring rest, renewal and rhythm."
  commitment10 = "*Daily Conscious Leadership commitment reminder: Opposite of my Story.* I commit to seeing that the opposite of my story is as true or truer than my original story. I recognize that I interpret the world around me and give my stories meaning."
  commitment11 = "*Daily Conscious Leadership commitment reminder: Approval.* I commit to being the source of my security, control and approval."
  commitment12 = "*Daily Conscious Leadership commitment reminder: Enough.* I commit to experiencing that I have enough of everything... including time, money, love, energy, space, resources, etc."
  commitment13 = "*Daily Conscious Leadership commitment reminder: Allies.* I commit to seeing all people and circumstances as allies that are perfectly suited to help me learn the most important things for my growth."
  commitment14 = "*Daily Conscious Leadership commitment reminder: Win for All.* I commit to creating win for all solutions (win for me, win for the other person, win for the organization, and win for the whole) for whatever issues, problems, concerns, or opportunities life gives me."
  commitment15 = "*Daily Conscious Leadership commitment reminder: Being the Resolution.* I commit to being the resolution or solution that is needed: seeing what is missing in the world as an invitation to become that which is required."


  schedule.every(5).seconds.do(lambda: sendCommitment(slack_client, commitment1))
  time.sleep(3)
  schedule.every(5).seconds.do(lambda: sendCommitment(slack_client, commitment2))


  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(1) # sleep for 1 second between checks




