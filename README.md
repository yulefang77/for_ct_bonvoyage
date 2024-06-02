# 將程式佈署至 Heroku

這份文件將指導你如何將你的程式部署到 Heroku，並且提供了後續串接 LINE Messaging API 的步驟。

## 前置作業

確保你已完成以下前置作業：
- 在本機成功測試程式。
- 下載並安裝 [Git](https://git-scm.com/download/win)。
- 完成 Heroku 官網註冊，並訂閱 Eco dynos plan。

## 安裝 Heroku Command Line Interface (CLI) 並驗證身份

1. 進入 [Heroku 官網教學設定網頁](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)。
2. 下載並安裝 Heroku CLI。
3. 開啟本機命令提示字元，輸入命令 `heroku login`。按照視窗指示完成身份驗證。
4. 這裡必須注意的是-「身份驗證」步驟，heroku 和 git 這兩個命令都必需正確運行才能成功。
 
## 在 Heroku 上建立新 app

1. 前往 [Heroku 儀表版](https://dashboard.heroku.com/apps)。
2. 點擊「create new app」按鈕，或者在右上角的 new 選單中選擇 create new app。
3. 在 App Name 欄位填入你的 app 名稱（可以任意）。
4. 完成後你將被導入 Deploy 網頁。
5. 佈署 app 這個步驟，我們先將環境變數設定完成再回來做。
6. 先選 settings 按鈕，前往設定 app 環境變數。
   
## 新 app 的環境變數設定 

1. 在 settings 頁面找到 Config Vars 區塊，點擊 Reveal Config Vars。
2. 將以下環境變數填入：
    - ACCESS_TOKEN
    - CHANNEL_SECRET
    - OPENAI_API_KEY
3. 請注意下面兩個資訊：
    - App Information > Heroku git URL，這是你要上傳程式的雲端位置。
    - Domains：這個區塊有一個以你的 app 名稱為首的網址，它就是你在雲端上提供服務的位置。

## 將程式佈署至 Heroku

1. 回到佈署程式網頁，點擊 deploy 按鈕。
2. 創建新 Git 倉庫 - Create a new Git repository
    - 下載程式所需檔案至專案資料夾，包括：
        - app.py
        - Procfile
        - requirements.txt
    - 在命令提示字元中進入專案資料夾，然後輸入以下指令：
    ```
    $ git init
    $ heroku git:remote -a 你的_app_名稱
    ```
3. 佈署你的應用程式 - Deploy your application
    - 提交程式碼至倉庫並使用 Git 將其部署到 Heroku。
    ```
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master
    ```
4. 完成第二步後，命令提示字元會輸出上傳與安裝程式的訊息。若無錯誤訊息產生，使用 `heroku logs --tail` 觀察日誌功能，確認佈署成功訊息。

## 串接 LINE Messaging API

1. 將 settings 網頁 > Domains 區塊裡 Heroku 提供服務的網址複製。
2. 回到使用者原先本機測式成功的 Line Bot Channel > Messaging API 網頁
3. 將步驟 1 服務網址貼到 Webhook settings > Webhook URL，記得網址結尾別漏掉 `/callback` 路由。
4. 按下 Verify 按鈕驗證是否成功。

## 後記

- 在這份文件中，上傳程式碼的指令與 Heroku 官網提供的指示有所不同，`git push heroku master` 和 `git push heroku main`。我測試的結果顯示，`git push heroku master` 可以成功上傳。
- 訂閱 Heroku Eco dynos plan 超過約 30 分鐘沒有流量，會進入睡眠。第一次測試 Webhook 驗證 Verify 按鈕可以喚醒服務，但可能會發生逾時回應錯誤。可以再按一次 Verify 按鈕測試程式是否成功回應。

## *祝你好運*
