from slack_bolt import App


def listners(app: App):

    # event("message"): メッセージ全般に反応
    # デバッグ用。不要になったらsayの行をコメントアウトする
    @app.event("message")
    def handle_message_events(event, say, logger):
        user = f"<@{event.get('user','ななしさん')}>"
        text = event.get('text', "")
        channel = f"<#{event.get('channel','知らないチャンネル')}>"

        # 返答内容を作成する
        reply_message = f"""
{user}さんが
{channel}で
{text}と
いいました。
"""

        # 返答する
        # say(reply_message)
