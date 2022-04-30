from slack_bolt import App


def listners(app: App):

    # event(): 投稿へのリアクション(stamp)全般に反応
    # ウザイのでコメントアウト
    @ app.event("reaction_added")
    def handle_reaction_added_events(event, say, logger):
        # stampがカレンダー(:calendar:)だったらカレンダーを表示してくれる
        if event["reaction"] == "calendar":
            say(
                blocks=[{
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "Pick a date for me to remind you"},
                        "accessory": {
                            "type": "datepicker",
                            "action_id": "datepicker_remind",
                            "initial_date": "2020-05-04",
                            "placeholder": {"type": "plain_text", "text": "Select a date"}
                        }
                        }],
                text="Pick a date for me to remind you"
            )
            pass
        # それ以外のstampだったら知らないとつぶやく
        else:
            say(f"I have no idea for that :{event['reaction']}:")
            pass
