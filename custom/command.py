from slack_bolt import App


def listners(app: App):

    # command(): ()内のアクションに反応する
    @app.command("/hello-bolt")
    def hello(body, ack):
        ack(f"Hi <@{body['user_id']}>!")
