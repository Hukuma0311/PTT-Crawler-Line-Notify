import urllib.request as rq
def geturl(url):
    ptt='https://www.ptt.cc'
    request=rq.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
        })
    with rq.urlopen(request) as rp:
        data=rp.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.findAll("div",class_="title")
    items=[]
    for title in titles:
        if title.a!=None:
            item=title.a.string
            item_url=ptt +title.find('a')['href']
            if "售" in item or "賣" in item or '特價' in item:
                combined=item+'\n'+item_url
                items.append(combined)
    return items
