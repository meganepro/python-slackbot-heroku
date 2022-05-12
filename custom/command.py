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

    @app.command("/drink-menu")
    def drink(ack, say, command):
        ack()
        user = f"<@{command.get('user_id','ななしさん')}>"
        text = command.get('text', "")
        channel = f"<#{command.get('channel_id','知らないチャンネル')}>"

        ################## write code here ##################
        say({
            "blocks": [
                {
                    "type": "input",
                    "element": {
                        "type": "radio_buttons",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Coffee :coffee:",
                                    "emoji": True
                                },
                                "value": "Coffee :coffee:"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Tea :teapot:",
                                    "emoji": True
                                },
                                "value": "Tea :teapot:"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Juice :beverage_box:",
                                    "emoji": True
                                },
                                "value": "Juice :beverage_box:"
                            }
                        ],
                        "action_id": "order-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What would you like to drink? :man-tipping-hand:",
                        "emoji": True
                    }
                }
            ]
        })
