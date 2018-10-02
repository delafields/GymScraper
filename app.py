from bs4 import BeautifulSoup
from twilio.rest import Client
import urllib.request
import datetime
import sys
import re
import os

def get_workout(url):
    # Soupify the page
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # Find the workout div and its p tags
    workout_box = soup.find('article', attrs={'class': 'article-index-1'})
    workout = workout_box.find_all('p')

    # stringify the soup
    res = ''
    for p in workout:
        res += str(p)

    # sub the <br/> and <p> tags with newlines
    rm_tags = re.compile('(</?p[^>]*>|<br/>)')
    text = rm_tags.sub('\n', res)

    return text


TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')
GYM_URL = os.environ.get('GYM_URL')


def text_workout():

    text = get_workout(GYM_URL)

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # text the workout
    client.api.account.messages.create(
        to = MY_NUMBER,
        from_ = TWILIO_NUMBER,
        body = text
        )

weekday = datetime.datetime.today().isoweekday()
# Sunday = 0 Saturday = 7
# If its sat or sun exit the program, else text
if weekday == 7 or weekday == 0:
    sys.exit()
else:
    text_workout()
