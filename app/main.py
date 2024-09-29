from http.client import ImproperConnectionState
import csv
from time import time
import requests
from buy import geturl
import time
from hot import receivepost 
import os
import logging
pathway=os.getcwd()

def post_data(message, token):
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        payload = {
            'message': message
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload
        )

    except Exception as _:
        print(_)

url_buy={
        "DC_SALE":['GR3','GRIII'], #設定關鍵字與對應子版
        "macshop":[['mac mini','m2'],['apple','tv'],'巧控板'], #可設定關鍵字交集(即同時符合才通知)
        } 

url_post=['Lifeismoney'] #設定欲檢查推文樹條件之子版
final=[]

try:
    while True:
        item_list=[]
        with open('output.csv','r',encoding='utf-8-sig') as check:
            rows=csv.reader(check)
            now=time.time()
            for r in rows:
                try:
                    item_list.append(r[1])
                except:
                    continue
            item_list2=set(item_list)
            check.close()
            if __name__ == "__main__":
                token = "PUT YOUR LINE NOTIFY TOKEN" # 您的 Line Notify Token
                for k in list(url_buy):
                    message = geturl(f'https://www.ptt.cc/bbs/{k}/index.html')
                    for i in message:
                        for kw in url_buy[k]:
                            if type(kw) != list:
                                if kw.upper() in i or kw in i or kw.lower() in i or kw.title() in i or kw.capitalize() in i:
                                    if i[i.index('\n'):] not in item_list2:
                                        with open('output.csv','a+',newline="",encoding="utf-8-sig") as f:
                                            writer=csv.writer(f)
                                            writer.writerow([i[:i.index('\n')],i[i.index('\n'):],time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),now])
                                            f.close()
                                            post_data(str(f'看板：{k}@{kw}\n\n{i}'), token)
                                            print('已通知',i[:i.index('\n')])
                            else:
                                    if kw[0].upper() in i or kw[0] in i or kw[0].lower() in i or kw[0].title() in i or kw[0].capitalize() in i:
                                        if kw[1].upper() in i or kw[1] in i or kw[1].lower() in i or kw[1].title() in i or kw[1].capitalize() in i:
                                            if i[i.index('\n'):] not in item_list2:
                                                with open('output.csv','a+',newline="",encoding="utf-8-sig") as f:
                                                    writer=csv.writer(f)
                                                    writer.writerow([i[:i.index('\n')],i[i.index('\n'):],time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),now])
                                                    f.close()
                                                    post_data(str(f'看板：{k}@{" ".join(kw)}\n\n{i}'), token)
                                                    print('已通知',i[:i.index('\n')])
                                        else:
                                            print('nope')
                                    
                                    
                for n in url_post:
                    post=receivepost(f'https://www.ptt.cc/bbs/{n}/index.html')
                    for p in post:
                        if p[2] not in item_list2:
                                if 'Lifeismoney' in p[2] and p[1]>40: #自訂推文數通知
                                    post_data(f'看板：{n}\n\n{p[0]}\n{p[2]}', token)
                                    with open('output.csv','a+',newline="",encoding="utf-8-sig") as f:
                                        writer=csv.writer(f)
                                        writer.writerow([p[0],p[2],p[1],'-'])
                                        f.close()

                    
                print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                time.sleep(60)
                now=time.time()
except:
    logging.error('oops',exc_info=True)
    print('System Failed, Restarting.')
