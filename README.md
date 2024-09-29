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
![自訂關鍵字](https://github.com/Hukuma0311/RPA-Demo/blob/main/pic/Sequence.jpg?raw=true)

*自訂推文數*  
![自訂推文數](https://github.com/Hukuma0311/RPA-Demo/blob/main/pic/Excel%20Process%20Scope.jpg?raw=true)


## 前置作業
您必須先在您的個人電腦上安裝UiPath Studio，如果您沒有安裝過的話，可以至[UiPath Automation CloudTM for Community](https://account.uipath.com/login?state=hKFo2SBjMW9RbmlXRFpFRWZUeGhpdjFHWG44SHFCMkJoYlFVSaFupWxvZ2luo3RpZNkgVTFaT2VacUhpM1V4N1BvTnpsbHdPNXU0eVl2RDRETk2jY2lk2SAyeXQ5SGRGNDVPMDA2SDlxZFBjUDlhczVjZEdibkNXcw&client=2yt9HdF45O006H9qdPcP9as5cdGbnCWs&protocol=oauth2&audience=https://uipath.eu.auth0.com/api/v2/&scope=openid%20profile%20email%20read:current_user%20update:current_user_metadata&redirect_uri=https://cloud.uipath.com/portal_/authCallback&type=signup&platform_name=UiPath%20Platform&subscription_plan=&ecommerceRedirect=false&retryUrl=&product_name=UiPath%20Automation%20Cloud&company_code=B2B_CP&cloudrpa_signup_subdomain=/portal_&register_endpoint=/register&use_local_registration=false&response_type=code&response_mode=query&nonce=SVJYcC5RWlFqdjNYRGdEbjhIZWouUmdVWkhUSVRIMFQ5RmJ4YkxXckMzUA%3D%3D&code_challenge=-Npc4KY4MeCfVXuWhpzLD6AQgNSsgBBpV4PVYgUYUic&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4yLjAifQ%3D%3D) 下載試用版本。（可能需要建立新帳號。）

## 安裝

1. 下載此repo並解壓縮。 

2. 用UiPath Studio打開名為 *Main.xaml* 的檔案並展開"sequence"

3. 點選 "Variables" 並在“stock”編輯您想要擷取資料的公司。 

4. 返回流程圖並打開"Excel Process Scope"，更改最終存檔位置至您想要存取的檔案位置。 

5. 發布此流程至您的本地資料夾（我個人建議發布到此檔案所在的資料夾）您將會看到副檔名為"nupkg"的檔案。

6. 利用Win+R開啟“執行”視窗並搜尋"AppData"，找到"UiRobot.exe"所在的資料夾，其應該會在 "C:\Users\[您的系統用戶名稱]\AppData\Local\Programs\UiPath\Studio"  

    複製該路徑。

 7. 利用文字編輯器編輯 "Main.bat" 批次檔，更改 [ ] 部分如下：

```bash
"C:\Users\[您的系統用戶名稱]\AppData\Local\Programs\UiPath\Studio\UiRobot.exe" execute --file "[此專案的存檔資料夾]\[您在發布專案時取的名稱].nupkg"
pause
```

8. 存檔，恭喜您，應該就可以正式使用了！