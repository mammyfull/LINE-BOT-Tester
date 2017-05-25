from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

BOT_CHANNEL_ACCESS_TOKEN = 'aCMtien4nmgo53rqyYwWeTAvQMzY4B2pIv2BhB3SrMgwIdb8rB7KtVAMqIElxlWIZmObi//TzcIVgdwBh7eO17/y18fBWGpT5IF/eLdRpNdvnJ5tj3rbccbCtHnDBXHs/Dgp0KjA6XNZZabDV4dGZwdB04t89/1O/w1cDnyilFU='
BOT_CHANNEL_SECRET = '5b7ae03cfb6d70312c43cfd629fd3aa2'


line_bot_api = LineBotApi(BOT_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(BOT_CHANNEL_SECRET)


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()