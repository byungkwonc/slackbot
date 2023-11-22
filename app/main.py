import logging

import uvicorn
from platform import system
from fastapi import FastAPI
from starlette.responses import Response
from .routers import chatgpt, slack

if system().lower().startswith("darwin"):
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(chatgpt.router, prefix="/openai", tags=["openai"])
app.include_router(slack.router, prefix="/slack", tags=["slack"])

logging.basicConfig(level=logging.INFO)

@app.get("/")
async def root():
    return Response("Hello ChatGPT Applications!")

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

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        #host="0.0.0.0",
        #port=8000,
        access_log=False,
        reload=True,
        timeout_keep_alive=60,
    )
