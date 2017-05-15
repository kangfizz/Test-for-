
# coding: utf-8

# In[58]:

#第一題
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/c.jpg",
    "http://www.google.com/b.txt",
    "http://www.facebook.com/movie/b.txt",
    "http://www.google.co.jp/a.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png"
]
testurl={}
for url in urls:
    if url[-5:] in testurl:
        testurl[url[-5:]]+=1
    else:
        testurl.update({url[-5:]:1})

for ss in sorted(testurl, key=lambda ia: testurl[ia], reverse=True)[:3]:
    print(ss+" "+str(testurl[ss]))
        


# In[63]:

#第三題
def anonymous(x):
    return x**2+1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept <end:
        intercept += step
        area+=anonymous(intercept)*step
    return area

print(integrate(anonymous, 0, 10))


# In[120]:

#ptt抓取
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.ptt.cc/bbs/car/index.html")
soup =  BeautifulSoup(response.text,"html.parser")
myurls=[]
container = soup.select('.r-ent')
i=0


for each_item in container:
     print ("日期："+each_item.select('div.date')[0].text, "作者："+each_item.select('div.author')[0].text 
           +" "+soup.select('a.board')[0].text)
     print (each_item.select('div.title')[0].text)
     urls=each_item.find_all('a', href=True)
     for url in urls:
        myurls.append("https://www.ptt.cc"+url['href'])
     response2 = requests.get(myurls[i])
     soup2 =  BeautifulSoup(response2.text,"html.parser")

     print(soup2.select("div#main-container")[0].text)
     i+=1



