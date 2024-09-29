<!-- 底下標籤來源參考寫法可至：https://github.com/Envoy-VC/awesome-badges#github-stats -->

<!--[](https://img.shields.io/github/stars/hsiangfeng/README-Example-Template.svg)｜![](https://img.shields.io/github/forks/hsiangfeng/README-Example-Template.svg)｜![](https://img.shields.io/github/issues-pr/hsiangfeng/README-Example-Template.svg)｜![](https://img.shields.io/github/issues/hsiangfeng/README-Example-Template.svg)-->


# 關鍵字爬取PTT.cc看板並傳遞到Line Notify

*注意: 此專案仍可運作但已停止更新*

<!--[專案封面圖](https://raw.githubusercontent.com/Hukuma0311/RPA-Demo/refs/heads/main/pic/logo.jpg)-->

## 說明

此自動化流程會訪問[批踢踢實業坊](https://www.ptt.cc/bbs/index.html)並定時爬取指定之看板與相對應之關鍵字，若出現符合條件之文章即傳送到個人之Line Notify

## 特色
* 可自訂特定看板與多個關鍵字  
* 可自訂推文數條件  
## 截圖


*自訂關鍵字*  
![自訂關鍵字](https://github.com/Hukuma0311/PTT-Crawler-Line-Notify/blob/main/screenshot/LINE_capture_749282636.426214.jpg?raw=true)

*自訂推文數*  
![自訂推文數](https://github.com/Hukuma0311/PTT-Crawler-Line-Notify/blob/main/screenshot/LINE_capture_749282645.285315.jpg?raw=true)


## 前置作業
您必須先建立自己的Line Notify權杖，可參考這篇教學[設定LINE Notify - CodiMD - Webduino](https://md.webduino.io/s/LCGRt1Jve)   
取得權杖後請保管好，稍後會用到
## 安裝

1. 下載此repo並解壓縮。 

2. 打開"main.py"，修改第57行的內容

```bash
token = "PUT YOUR LINE NOTIFY TOKEN" # 將您的Line Notify權杖貼在""內
```

3. 若要修改關鍵字與看板，請更改第31行的內容  
例：想收到DC_Sale的「GR3」買賣文章 與 MacShop的「M2版本Mac Mini」與「巧控板」買賣文章

```bash
url_buy={
        "DC_Sale":['GR3','GRIII'], #設定關鍵字與對應子版
        "MacShop":[['Mac Mini','M2'],'巧控板'], #可設定關鍵字交集(即同時符合才通知)
        } 
```

4. 若要修改推文條件與看板，請更改第36行與85行的內容
例：想收到Lifeismoney推文超過40以上的最新文章    

```bash
url_post=['Lifeismoney'] #設定欲檢查推文樹條件之子版
```
```bash
if 'Lifeismoney' in p[2] and p[1]>40: #自訂推文數通知
```
5. 存檔，恭喜您，應該就可以正式使用了！