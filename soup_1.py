# -*- coding: cp936 -*-
import urllib
import re
import string
from BeautifulSoup import BeautifulSoup
def HouseRow(houserow):
    house = houserow.find('div',{'class':'house'})
    money =house.money.strong.string
    print "price is %s for this house" ,money
#http = 'http://zu.wuhan.soufun.com/house-xm2610337706/'
http = "baolihuadu.html"
html_src = urllib.urlopen(http).read()
#local_file = file("baolihuadu.html","a")
#local_file.write(html_src)
#parser = BeautifulSoup(html_src)
parser = BeautifulSoup(html_src,fromEncoding='gb18030')
house_list = parser.find('div',{'class':'bkyellow'})
HouseRow(house_list)
#house = house_list.find('div',{'class':'house'})
#house_money = house.find('dd',{'class':'money'})
#print house_money.find('strong').contents[0].name
#price = house_money.strong.contents
#print house_money.strong.contents
#print "string is", house_money.strong.string 
#price = price * 2
#str = '200'
#print string.atoi(price)
#print house_list
#print house_inf
#print house.find()
#print "\nfinished\n"
#print house_list
#print html_src

def HouseRow(houserow):
    house = houserow.find('div',{'class':'house'})
    money =house.money.strong.string
    print "price is %s for this house" ,money
    
