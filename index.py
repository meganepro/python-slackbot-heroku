import logging
logging.basicConfig(level=logging.DEBUG)
import os
from slack_bolt import App as SlackBolt
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request


# boltの初期化
bolt = SlackBolt(
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    token=os.environ.get("SLACK_BOT_TOKEN")
)


# Flask アプリを初期化
app = Flask(__name__)
handle = SlackRequestHandler(bolt)


# Flask アプリへのルートを登録します
@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handle.handle(request)


##########################################################################
# custom actionの設定
import custom.message
custom.message.listners(bolt)
import custom.event_action
custom.event_action.listners(bolt)
import custom.event_mention
custom.event_mention.listners(bolt)
import custom.event_message
custom.event_message.listners(bolt)
import custom.event_stamp
custom.event_stamp.listners(bolt)
import custom.command
custom.command.listners(bolt)
##########################################################################


# ローカルでのアプリの起動設定
if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
