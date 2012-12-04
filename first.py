# -*- coding:gb2312 -*-  
import urllib,sys  
from BeautifulSoup import BeautifulSoup
#reload(sys)  
#sys.setdefaultencoding("gb2312")
httpq = ['http://zhidao.baidu.com/question/189027634.html']
print "hi here"
def iskey(strr):
    print "iskey start"
    keys = ["导演","演员","电影"]
    for key in keys:
        if(strr.find(key) != -1):
            return 0
    return -1

def getCon(http):
    print "getCOn start"
    html_src = urllib.urlopen(http).read()

    parser = BeautifulSoup(html_src.decode("gb2312","ignore"))

    question = parser.find("span","question-title")

    answer = parser.find("pre",attrs={'id':'best-answer-conten'})

    if answer is None:
        no = -1
    else:
        f = file("page.txt","a")

        f.write("Q:%s\n" % question.contents[0].encode("gb2312"))
        f.write("A:%s\n" % answer.contents[0].encode("gb2312"))

        f.close()

    base = "http://zhidao.baidu.com"

    urls = parser.findAll("a",attrs={'log':'relative.title.click'})

    for url in ruls:
        str = url.contents[0]
        if(isKey(str) != -1):
            newHttp = base+url['href']
            httpq.append(newHttp)
    print "getCon finished"

def main():
    print "main start"
#    while len(httpq) != 0:
#    getCon(httpq.pop(0))
    print "main finished"

#if __name__ =='__main__':main()
main()
