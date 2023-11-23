# Building an app with Bolt for Python

## Bolt for Python
- [Bolt for Python](https://slack.dev/bolt-python/concepts)

## Getting Started

### Creating a Slack App
- https://api.slack.com/apps?new_app=1&ref=bolt_start_hub

### Requesting scopes
- OAuth & Permissions > Bot Token Scopes
- Add an OAuth Scope, Add the `chat:write` scope

### Installing your app
- Install App To Workspace
- OAuth & Permissions > Bot User OAuth Access Token > Copy!!

### Enable your app's home
- Home tabs

## Local Environment

### virtual environment
- create `python3 -m venv .venv`
- activate `source .venv/bin/activate`

### app credentials
- `SLACK_BOT_TOKEN`
- `SLACK_SIGNING_SECRET`

## Developing your app

### Installing the Bolt Python package
- `pip install slack_bolt`

### Initializing your app
```
import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
# @app.event("app_home_opened") etc


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

```
- run `python3 main.py`

## Subscribing to events

### Event Subscriptions
- Request URL : `https://slackbot-chatgpt.vercel.app/slack/events`
- subscribe to the `app_home_opened` event

## Responding to events

### set up a basic listener
- using the `app_home_opened` event
- publishes a view to your Home tab

### listener code
```
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )

  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")

```
- run `python3 main.py`