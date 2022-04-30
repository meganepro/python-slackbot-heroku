from slack_bolt import App


def listners(app: App):

    # message(): ()内の投稿を拾って反応してくれるユーザーの文言を拾ってくれる ※mention不要
    @app.message("hello")
    def reply_hello(message, say):
        user = f"<@{message.get('user','ななしさん')}>"
        text = message.get('text', "")
        channel = f"<#{message.get('channel','知らないチャンネル')}>"

        ################## write code here ##################
        say("Hey there " + user + ", at " + channel + "!")
