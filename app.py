import os
from dotenv import load_dotenv
from flask import Flask, request, abort
from openai import OpenAI
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

# 載入 .env 檔案內容 
load_dotenv()

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')
BONVOYAGE = os.environ.get('BONVOYAGE')

app = Flask(__name__)

configuration = Configuration(access_token=ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        user_text = event.message.text
        openai_msg = call_openai_api(user_text)

        if openai_msg:
            pass
        else:
            # 呼叫 openai api 失敗，直接回傳使用者訊息
            openai_msg = user_text

        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=openai_msg)]
            )
        )

def call_openai_api(user_text):
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": (
                    "你是一位生活助手，稱呼使用者「老闆」，"
                    "回答應以像職場下屬對上司的態度回應使用者:"
                    "尊敬的、理解的、信任的。中文回答使用正體中文字，勿使用簡體字。"
                    f"回答長度不要超過200個字。{BONVOYAGE}"
                )},
            {"role": "user", "content": user_text}
          ]
        )
        openai_msg = completion.choices[0].message.content
    
        return openai_msg
    
    except Exception as e:
        print("Exception when calling call_openai_api->get_profile: %s\n" % e)

        return None


if __name__ == "__main__":
    app.run()


