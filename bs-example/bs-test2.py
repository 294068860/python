#import urllib.request
import urllib
import chardet
from bs4 import BeautifulSoup

#获取该页面所有链接
url="http://www.shicimingju.com/book/sanguoyanyi.html"
content = urllib.urlopen(url).read()
#print content

def Fun1():
    soup = BeautifulSoup(content, 'html.parser')
    for v in soup.select('.book-mulu ul li'):
        #print str(v)
        #print v.get_text()
        #for v2 in v.select('a[href]'):
            #print str(v2)
            #print v2.get_text()
            #print v2.attr('href')
        data_array = v.find_all('a')
        for data in data_array:
            print data['href']
def Fun2():
    soup = BeautifulSoup(content, 'html.parser')
    menu = soup.find_all(attrs={'class':'book-mulu'})
    for v in menu:
        print str(v)
        menu2 = v.find_all('li')
        for v2 in menu2:
            print str(v2)
            menu3= v2.find_all('a')
            for v3 in menu3:
                print str(v3)
                menu4 = v3.find_all('href')
                for v4 in menu4:
                    print str(v4)

#Fun1和Fun2是测试方法
#Fun3是最简单的方法
def Fun3():
    soup = BeautifulSoup(content, 'html.parser')
    for data1 in soup.select('.book-mulu'):
        data2 = data1.find_all('a')
        for data3 in data2:
            print data3['href']
Fun3()
