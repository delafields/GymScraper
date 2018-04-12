from bs4 import BeautifulSoup
from twilio.rest import Client
import urllib.request
import re
import os

# Soupify the page
url = 'https://www.districtcrossfit.com/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# Find the workout div and its p tags
workout_div = soup.find('div', attrs={'class': 'summary-excerpt'})
workout = workout_div.find_all('p')

# stringify the soup
res = ''
for p in workout:
    res += str(p)

# sub the <br/> and <p> tags with newlines
rm_tags = re.compile('</*(p|br)/*>')
text = rm_tags.sub('\n', res)

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client.api.account.messages.create(
    to = MY_NUMBER,
    from_ = TWILIO_NUMBER,
    body = text
    )

print(text)
