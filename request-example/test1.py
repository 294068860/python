# -*- coding: utf-8 -*-
import requests
import re

root_url='http://www.kiees.com/'
global_cnt=1

#图片写入文件
def writeJPG(name, url):
    data = requests.get(url)
    with open(name,'wb') as file:
        file.write(data.content)
        file.close()


#获得每个页面的子页面
def getPageUrl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400'}
    r = requests.get(url, headers=headers)
    content = r.content
    data_array = re.findall(r"class=\"a_img\" href=\"(.+?)html", content)
    for data in data_array:
        #print data
        #print root_url + data + 'html'
        getPageContent(root_url + data + 'html')     

#获得每页子页面的内容
def getPageContent(url):
    global global_cnt
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400'}
    r = requests.get(url, headers=headers)
    content = r.content
    #print 'data:\n' + content
    data_array = re.findall(r"<h3>(.+?)<span", content) 
    #获得文章标题
    for data in data_array:
        print str(global_cnt) + ' : ' + data.decode("utf-8")
        global_cnt = global_cnt + 1
    #获得购买链接    
    data_array = re.findall(r"tracklink\" rel=\"nofollow\" target=\"_blank\" href=\"(.+?)\">", content)
    for data in data_array:
        print u"购买链接:" + data
	
    #获得商品图片 
    data_array = re.findall(r"<img src=\"(.+?)\"", content)
    #for data in data_array:
    print u"商品图片:" + data_array[2]
    writeJPG('download\\' + str(global_cnt-1) + '.jpg', data_array[2])
    
        
def myMain():
    for i in range(1,100):
        if i == 1:
            url = root_url
        else:
            url = root_url + "index" + str(i) + ".html"
            
        getPageUrl(url)

myMain()
#getPageContent('http://www.kiees.com//2018/05/02/654411.html')
