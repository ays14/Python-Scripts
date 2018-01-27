import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.billboard.com/charts/hot-100'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#name_box = soup.find('div', attrs={'class':''})
#name = name_box.text.strip()
#print name

hotSong=[]
for song in soup.find_all('h2',attrs={'class':'chart-row__song'}):
	s=song.text.strip()
	hotSong.append(s)


#hotArtist=[]
#for artist in soup.find_all('span', attrs={'class':'chart-row__artist'}):
#	a=artist.text.strip()
#	hotArtist.append(a)

#print 'len=',len(hotArtist)
#print 'len2=',len(hotSong)

for i in range(0,50):
	print i+1,
	print '-',
	print hotSong[i]

#	print hotArtist[i]
