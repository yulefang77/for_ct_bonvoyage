# 在本機測試 Line Messaging API 串接 OpenAI API 的範例程式
本範例假設使用者已取得 OpenAI API key。
# 前置作業
# LINE Developers 流程
1. 到 [LINE Developers](https://developers.line.biz/) 註冊。
2. 創建提供者 (provider)。
3. 在新建的提供者底下創建一個新的頻道 (Messaging API)：
    - 每個頻道代表一個機器人。
    - 每個提供者可以管理一個以上的頻道。
    - 在新建的 Messaging API 頻道中：
        1. Basic setting 可以取得 *Channel secret*。
        2. Messaging API 可以取得 *Channel access token* (第一次需要自行發布)。
# ngrok 流程
1. 到 [ngrok](https://www.example.com) 註冊。
2. 下載 ngrok。
3. 將你的 authtoken 加到 default ngrok.yml。
    - 點選登入頁面的左方 getting started -> [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) 頁面。
    - 複製 Command Line 指令並執行。

        ```
        ngrok config add-authtoken your_auth_token
        ```

# 程式前置作業
1. 安裝程式必要模組：
    - dotenv (載入環境變數用)。
    - flask。
    - openai。
2. 建立 .env 檔，將取得的 token 寫入環境變數：
    - *OPENAI_API_KEY*。
    - *ACCESS_TOKEN*。
    - *CHANNEL_SECRET*。
3. 執行前檢查檔案，本範例僅需要 2 個檔案：
    - *app.py*。
    - *.env*。

# 執行程式
1. ***flask***：在*命令提示字元*視窗執行 `flask run` ，在本機啟動服務。這時會有一行訊息表示程式已啟動服務，埠口為 5000。

    > Running on http://127.0.0.1:5000

2. ***ngrok*** 
    - 執行 ngrok 會跳出一個 *Windows PowerShell* 視窗。
    - 執行指令 `ngrok http 5000` 程式執行後、尋找 Forwarding 這行訊息。它會如下所示。https://4d2f-123-456-00-789.ngrok-free.app 即為本機對外服務的網址。 

        > Forwarding                    https://4d2f-123-456-00-789.ngrok-free.app -> http://localhost:5000
       
# 回到 [LINE Developers](https://developers.line.biz/) 設定 webhook。
在 line channel->messaging api 找到webhook 設定：
1. Webhook settings
    - Webhook URL 填入 ngrok 提供網址並加上 `/callback` 如下：
      
        ```
        https://4d2f-123-456-00-789.ngrok-free.app/callback
        ```
        
    - 打開 use webhook。
    - 點擊 Verify 。如果跳出 success 視窗，即表示已串接成功。如果這裡發生錯誤，通常是 access token 或 channel screcet 環境變數未設定正確。
    - 使用上方 Bot information： *Bot basic ID* 或 *QR code* 擇一方式加入好友。
    - 傳一份文字訊息測試是否成功。 如果串接失敗，會回傳與使用者一樣的訊息。如果這裡發生錯誤, 錯誤訊息可以到 flask *命令提示字元*視窗找到。

2. LINE Official Account features (可跳過這個步驟)
    - 關閉 Auto-reply messages
# *Good Luck!*
