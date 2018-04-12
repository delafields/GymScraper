from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://www.districtcrossfit.com/'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

workout_box = soup.find('div', attrs={'class': 'summary-excerpt'})

test = workout_box.find_all('p')
vals = []
for child in test:
    vals.append(str(child))

text = ''.join(vals)

rm_tags = re.compile('</*(p|br)/*>')
new = rm_tags.sub('\n', text)

print(new)
