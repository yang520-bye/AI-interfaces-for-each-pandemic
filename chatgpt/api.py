import json
import uuid
from datetime import datetime

import requests

current_timestamp = datetime.now().timestamp()
one_hour_later_timestamp = current_timestamp + 3600  # 3600秒等于一个小时

def read_cookie():
    with open('cookie.txt', 'r', encoding='utf-8') as file:
        cookie = file.read()
    return cookie



hearders = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJwYW44MTQ5MTNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy04TWs1YU1WNkg2UnVSWW5YQUJtS3BKVU0iLCJ1c2VyX2lkIjoidXNlci1Ra2F0NXAwUnJRT1g0bnlEekV3WUpJZEUifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MjU1NzY5ODYxODQxMDk5Njk3IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMDA4NDkzMiwiZXhwIjoxNzEwOTQ4OTMyLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSBvZmZsaW5lX2FjY2VzcyJ9.1YafjdyGcncFp4pDCF7ixj5RYequllWCaIjZvX9B7A1Z6C4li0yrD3ML1fjPMCp5wg31Pj__CgytDGmUCKeMCg33hHX9CYm_t-jt0hSvppkpM9jl9FUMFwiKWAOX27e_E03Fc3QgvcunHSqhEXASfBkyX9uTFYFKJjPtzST0QkX15Jh65wKw0KP-qAL7NT_LLKJbhIXmyvNyLZ9SuhBdT0EWsWIyFE-7HYnv-LN4R-DLieGuHb0rYYCp6lA6bqrtH9N-AcQdzgBRxMWYoWbMZXjBtnOyJb6xnYz-_RYnCWUiQj1a2JgPlHrxf7h9U-ww0K4E64AEw4g3l9TmSLJXbg',
    'Cookie': read_cookie() ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    "Content-Type": "application/json"
}


# 新建会话id
def make_new_conversation_id():
    message_id = str(uuid.uuid4())
    datas = {
        "action": "next",
        "conversation_mode": {"kind": "primary_assistant"},
        "force_paragen": False,
        "force_rate_limit": False,
        "history_and_training_disabled": False,
        'parent_message_id': message_id,
        "model": "text-davinci-002-render-sha",
        "suggestions": [],
        "timezone_offset_min": -480,
    }
    r = json.loads(requests.post('https://chat.openai.com/backend-api/conversation', headers=hearders,
                                 data=json.dumps(datas)).text)
    conversation_id = r.get('conversation_id')
    # wss_url = r.get('wss_url')
    return conversation_id


# 发送消息
def sends(msg, conversation_id):
    message_id = str(uuid.uuid4())
    datas = {
        "action": "next",
        "conversation_id": conversation_id,
        "conversation_mode": {"kind": "primary_assistant"},
        "force_paragen": False,
        "force_rate_limit": False,
        "history_and_training_disabled": False,
        "messages": [
            {
                "id": message_id,
                "author": {"role": "user"},
                "content": {"content_type": "text", "parts": [msg]},
                "content_type": "text",
                "parts": [msg],
                "metadata": {}
            }
        ],
        "model": "text-davinci-002-render-sha",
        "suggestions": [],
        "timezone_offset_min": -480,
    }
    r = json.loads(requests.post('https://chat.openai.com/backend-api/conversation', headers=hearders,
                                 data=json.dumps(datas)).text)
    wss_url = r.get('wss_url')
    return wss_url
