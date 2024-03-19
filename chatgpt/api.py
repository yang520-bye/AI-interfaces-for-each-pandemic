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

def read_auth():
    with open('authorization.txt', 'r', encoding='utf-8') as file:
        auth = file.read()
    return auth
    

hearders = {
    'Authorization': read_auth(),
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
