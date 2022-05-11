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

    @app.message("いめーじさんぷる")
    def reploy_image_sample(message, say):
        user = f"<@{message.get('user','ななしさん')}>"
        text = message.get('text', "")
        channel = f"<#{message.get('channel','知らないチャンネル')}>"

        ################## write code here ##################
        # https://app.slack.com/block-kit-builder/T03CPLVRW4S#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22This%20is%20a%20plain%20text%20section%20block.%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22image%22,%22image_url%22:%22https://i1.wp.com/thetempest.co/wp-content/uploads/2017/08/The-wise-words-of-Michael-Scott-Imgur-2.jpg?w=1024&ssl=1%22,%22alt_text%22:%22inspiration%22%7D%5D%7D
        say({
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "This is a plain text section block.",
                        "emoji": True
                    }
                },
                {
                    "type": "image",
                    "image_url": "https://i1.wp.com/thetempest.co/wp-content/uploads/2017/08/The-wise-words-of-Michael-Scott-Imgur-2.jpg?w=1024&ssl=1",
                    "alt_text": "inspiration"
                }
            ]
        })
