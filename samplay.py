# -*- coding: cp936 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import re
import string

http = "temp.html"
html_src = urllib.urlopen(http).read()
soup = BeautifulSoup(html_src,fromEncoding='gb18030')
#print soup
house = soup.find('div',{'class':'house'})
house_inf = house.dl.dt
black_1, black_2 = house_inf.findAll('p',{'class':'black'})
print black_2
print "\nfinished"
print type(house)
print type(house_inf)
print type(black_1)
zu = black_2.find('span').string
print zu
pingmi = u'平米'
print re.sub(pingmi,'',zu)

#print string.atoi(zu)
#print soup.contents[0].contents[0].name
#print soup.prettify()
# <html>
#  <head>
#   <title>
#    Page title
#   </title>
#  </head>
#  <body>
#   <p id="firstpara" align="center">
#    This is paragraph
#    <b>
#     one
#    </b>
#    .
#   </p>
#   <p id="secondpara" align="blah">
#    This is paragraph
#    <b>
#     two
#    </b>
#    .
#   </p>
#  </body>
# </html>
