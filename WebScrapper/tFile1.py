import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.billboard.com/charts/hot-100'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

hotSong=[]
for song in soup.find_all('div',attrs={'class':'chart-row__title'}):
	s=song.text.strip()
	hotSong.append(s)

print '--------------------------------------------------------------------------------------'

for i in range(len(hotSong)):
	print i+1,
	print '-',
	print hotSong[i]
	print '--------------------------------------------------------------------------------------'