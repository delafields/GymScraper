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

account_sid = 'XXX'
auth_token = 'XXX'

client = Client(account_sid, auth_token)

client.api.account.messages.create(to = '+XXX', from_ = '+XXX', body = text)

print(text)
