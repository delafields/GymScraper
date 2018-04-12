from bs4 import BeautifulSoup
import urllib.request
import re

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

print(text)
