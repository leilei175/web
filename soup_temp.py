# -*- coding: cp936 -*-
import urllib
import string
import re
from BeautifulSoup import BeautifulSoup

def GetDate(HtmlUrl):
    html_src = urllib.urlopen(HtmlUrl).read()
    html_src = BeautifulSoup(html_src,fromEncoding='gb18030')
    house_list = html_src.find('div',{'class':'bkyellow'})

def Getprice(HtmlUrl):
    html_src = urllib.urlopen(HtmlUrl).read()
    html_src = BeautifulSoup(html_src,fromEncoding='gb18030')
    house_list = html_src.find('div',{'class':'bkyellow'})
    house = house_list.find('div',{'class':'house'})
    house_money = house.find('dd',{'class':'money'})
    price = house_money.strong.string
    price =  string.atoi(price)
   # print("price is %s" %price%"平米\n")
    print price
    return price

def GetSize(HtmlUrl):
    html_src = urllib.urlopen(http).read()
    soup = BeautifulSoup(html_src,fromEncoding='gb18030')
    house = soup.find('div',{'class':'house'})
    house_inf = house.dl.dt
    black_1, black_2 = house_inf.findAll('p',{'class':'black'})
#    print black_2
#    print "\nfinished"
#    print type(house)
#    print type(house_inf)
#    print type(black_1)
    zu = black_2.find('span').string
#    print zu
    pingmi = u'平米'
    size = re.sub(pingmi,'',zu)
    size = string.atoi(size)
    print ("size is %s" %size%"平米\n")
    return size
    

#to get all the info of this house from the given page
def GetTheHouseInf(HtmlUrl):
    community = GetCommunity(HtmlUrl)
    date = GetDate(HtmlUrl)
    name = GetName(HtmlUrl)
    price = GetPrice(HtmlUrl)
    size = GetSize(HtmlUrl)
    romm = GetSquare(HtmlUrl)
    print ("community is %s,\n", communicty)
    print ("date is %s,\n", date)
    print ("name is %s,\n",name)
    print ("price is%s,\n",price)
    print ("size is %s,\n",size)
    print ("room is %s,\n",room)

http = "baolihuadu.html"

Getprice(http)
GetSize(http)


#html_src = urllib.urlopen(http).read()
#html_src = BeautifulSoup(html_src,fromEncoding='gb18030')
#house_list = html_src.find('div',{'class':'bkyellow'})                           
#house = house_list.find('div',{'class':'house'})
#获得housetitle段数据
#house_inf_1 = house.p
#housetitle = house_inf_1.a.strong.string

#house_inf_2 = house.
#print housetitle

#house_inf_2,second = house.findAll('p',{'class':'black'})
#print house_inf_2[1]
#print "\n\nfinished\n"

