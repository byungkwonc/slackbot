#pip install slack_bolt

import os
from slack_bolt import App

app = App(
    slack_token = os.environ.get("slack_token"),
    _secret = os.environ.get("SLACK_SIGNING_SECRET") 
)

if __name__ == "__main__":
    app.start(
        port = int(os.environ.get("PORT", 3000))
    )