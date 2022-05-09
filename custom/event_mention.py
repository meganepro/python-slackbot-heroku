from slack_bolt import App
from custom.util import is_include


def listners(app: App):
    # botにメンションがつけられた場合に反応
    @app.event("app_mention")
    def reply_mention_hello(event, say):
        user = f"<@{event.get('user','ななしさん')}>"
        text = event.get('text', "")
        channel = f"<#{event.get('channel','知らないチャンネル')}>"

        ################## write code here ##################
        if(is_include(text, "おみくじ")):
            kekka = uranai()
            say(user + " さんは " + kekka + "です！")
        else:
            say(user + "さん、よびました？？")

    # uranai結果を返す
    def uranai():
        import random
        number = random.randrange(1, 11)
        uranai = "大凶 :skull_and_crossbones:"
        if number <= 1:
            uranai = "大吉 :tada:"
        elif number <= 3:
            uranai = "中吉 :mega:"
        elif number <= 7:
            uranai = "吉 :neutral_face:"
        elif number <= 9:
            uranai = "凶 :ghost:"
        print("おみくじの結果→→→→→→→→→→" + uranai)

        return uranai
