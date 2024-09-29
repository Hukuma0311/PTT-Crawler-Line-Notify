import urllib.request as rq
import csv
import datetime as dt
import time

def receivepost(url):
    ptt='https://www.ptt.cc'
    n=0
    list=[]
    while n<3:
        request=rq.Request(url,headers={
            "cookie":"over18=1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
            })
        with rq.urlopen(request) as rp:
            data=rp.read().decode("utf-8")
        import bs4
        root=bs4.BeautifulSoup(data,"html.parser")
        push=root.findAll("div",class_='r-ent')
        for p in push:
            if p.a!=None:
                if p.find('span',class_='hl f3') != None:
                    pn=p.find('span',class_='hl f3')
                    pn=pn.text
                    title=p.find('div',class_='title')
                    t=title.a.string
                    u=title.find('a')['href']
                    if "公告" not in t:
                        list.append([t,int(pn),str(ptt+u)])
                if p.find('span',class_='hl f1') != None:
                    pn=p.find('span',class_='hl f1')
                    pn=pn.text.replace('爆',str(100))
                    title=p.find('div',class_='title')
                    t=title.a.string
                    u=title.find('a')['href']
                    if "公告" not in t:
                        list.append([t,int(pn),str(ptt+u)])
        n+=1
        url=ptt+root.find('a',string='‹ 上頁')['href']

    return list