# slackbot
[client]
- slack api로 bot을 생성
- slack workspace에 생성한 app 추가

[server]
- slack에서 message가 전송되면,
- OpenAI ChatGPT API로 response를 생성하여 slack에 전달

# 환경변수
- slack_token
- openai_token
- number_of_messages_to_keep
- system_content

## Local 실행
1. local 환경 구성
```bash
pip install -r requirements.txt
```

2. application 실행
```bash
uvicorn app.main:app --reload
```
## API Documentation
- `http://127.0.0.1:8000/docs`
