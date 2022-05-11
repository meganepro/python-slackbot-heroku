from slack_bolt import App
from custom.util import is_include, extract


def listners(app: App):
    # botにメンションがつけられた場合に反応
    @app.event("app_mention")
    def reply_mention_hello(event, say):
        user = f"<@{event.get('user','ななしさん')}>"
        text = event.get('text', "")
        channel = f"<#{event.get('channel','知らないチャンネル')}>"

        ################## write code here ##################
        # おみくじ
        if(is_include(text, "おみくじ")):
            kekka = uranai()
            say(user + " さんは " + kekka + "です！")
        # 郵便番号から住所
        elif(is_include(text, "の住所は？")):
            zipcode = extract(text, "", "の住所は")
            if zipcode:
                place = zipcode2address(zipcode)
                # 住所が取得できた場合
                if place:
                    say(place + "です！")
                else:
                    say("住所がうまく検索できませんでした！")
            else:
                say("郵便番号がよくわかりませんでした！")
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


# zipcodeを住所に変換する
def zipcode2address(zipcode: str):
    import json
    import requests
    response = requests.get("https://zipcloud.ibsnet.co.jp/api/search", params={"zipcode": zipcode})
    results = json.loads(response.text)
    # 住所が取れなかった場合はNone（なにもない）を返す
    if (results['results'] is None):
        return None
    # 住所が取得できた場合の処理
    result = results['results'][0]
    address = result['address1'] + result['address2'] + result['address3']
    return address


if __name__ == "__main__":
    print(zipcode2address("15000011"))
