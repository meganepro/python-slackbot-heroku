from slack_bolt import App


def listners(app: App):

    # command(): ()内のアクションに反応する
    @app.command("/hello-bolt")
    def hello(ack, say, command):
        ack()
        user = f"<@{command.get('user_id','ななしさん')}>"
        text = command.get('text', "")
        channel = f"<#{command.get('channel_id','知らないチャンネル')}>"

        ################## write code here ##################
        say(f'Hi! {user}! at {channel}.\nYou say {text}')
