from slack_bolt import App


def listners(app: App):

    # @app.action(<action-id>)に一致したら呼び出される
    # 「Interactivity & Shortcuts」の設定＆ReInstallも必要
    @app.action("order-action")
    def handle_order_action(ack, say, body):
        ack()
        user = f"<@{body.get('user',{}).get('id','ななしさん')}>"
        value = body["actions"][0]["selected_option"]["value"]

        ################## write code here ##################
        # 返答内容を作成する
        say(f'{user}さん！ヘイお待ち！\n{value}')
