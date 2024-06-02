# 將程式佈署至 Heroku
本文假設使用者已完成以下前置作業
- 成功在本機測試程式成功
- 成功下載安裝 [Git](https://git-scm.com/download/win)
- 完成 Heroku 官網註冊，並訂閱 Eco dynos plan
## 下載安裝 Heroku Command Line Interface (CLI) 並驗證身份
- 進入 [Heroku 官網教學設定網頁](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- 下載安裝 Heroku CLI
- 按照設定網頁指示，開啟本機命令提示字元，鍵入命令 `heroku login`。按照視窗指示隨意按一個鍵，此命令會將您的網絡瀏覽器打開到 Heroku 登錄頁面。如果您的瀏覽器已經登錄到 Heroku，只需單擊頁面上顯示的“Login in”按鈕即可。
- 必須注意的是-這個身份驗證步驟，heroku 和 git 這兩個命令都必需正確運行才能成功。
## 在 Heroku 上建立新 app
- 回到 [Heroku 儀表版](https://dashboard.heroku.com/apps)
- 使用者會看到 create new app 按鈕，或者它會放網頁右上方有一個 new 選單裡面
- 進入 create new app 網頁，在 App Name 欄位填入使用者 app 名稱。(可任意)
- 完成這個步驟，使用者會被導入 Deploy 網頁。
- 佈署 app 這個步驟，我們最後將環境變數設定再回來做。先選 settings 按鈕，前往設定 app 環境變數。 
## 新 app 的環境變數設定 
- 假設使用者在已經正確導至 settings 網頁，在 Config Vars 區塊點選 Reveal Config Vars，將環境變數填進去。
    - ACCESS_TOKEN
    - CHANNEL_SECRET
    - OPENAI_API_KEY
- settings 網頁還有2個資訊必須要注意。
1. App Information > Heroku git URL，這個是等一下你要上傳程式的雲端位置。
2. Domains：這個區塊有一個以使用者 app 命名稱為首的網址，它就是你在雲端上提供服務的位置。
## 將程式佈署至 Heroku
點選 deploy 按鈕回到佈署程式網頁，按照指示佈署程式。
1. 創建新 Git 倉庫 - Create a new Git repository
    - 將本分支需要用到的檔案下載至專案資料匣，它包含
        - app.py
        - Procfile
        - requirements.txt
    - 在命令提示字元視窗進入專案資料匣，然後輸入以下指令
    ```
    $ git init
    $ heroku git:remote -a user's_app_namm
    ```
2. 佈署使用者的應用程式 - Deploy your application
    - 將程式碼提交到存儲庫並使用 Git 將其部署到 Heroku。
    ```
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master
    ```
3. 完成第二步驟以後，命令提示字元視窗會輸出一連串上傳與安裝程式訊息。若無錯誤訊息產生，接著使用 `heroku logs --tail` 觀察日誌功能，確認佈署成功訊息。

## 後記
- 我提供的說明文件中，上傳程式碼與網頁有一些不同，`git push heroku master` 與 `git push heroku main`，這個是預設分支的名稱問題。不熟悉 Git 操作的初學者容易被困在專案分支這個問題上。我測試的結果，`git push heroku master` 才可以成功上傳。Heroku 官網針對該問題也有提供[解決方案](https://help.heroku.com/O0EXQZTA/how-do-i-switch-branches-from-master-to-main)
## Good Luck for C.T.
