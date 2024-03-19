import json
import uuid
from datetime import datetime

import requests

current_timestamp = datetime.now().timestamp()
one_hour_later_timestamp = current_timestamp + 3600  # 3600秒等于一个小时

hearders = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJwYW44MTQ5MTNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy04TWs1YU1WNkg2UnVSWW5YQUJtS3BKVU0iLCJ1c2VyX2lkIjoidXNlci1Ra2F0NXAwUnJRT1g0bnlEekV3WUpJZEUifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MjU1NzY5ODYxODQxMDk5Njk3IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMDA4NDkzMiwiZXhwIjoxNzEwOTQ4OTMyLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9yZ2FuaXphdGlvbi53cml0ZSBvZmZsaW5lX2FjY2VzcyJ9.1YafjdyGcncFp4pDCF7ixj5RYequllWCaIjZvX9B7A1Z6C4li0yrD3ML1fjPMCp5wg31Pj__CgytDGmUCKeMCg33hHX9CYm_t-jt0hSvppkpM9jl9FUMFwiKWAOX27e_E03Fc3QgvcunHSqhEXASfBkyX9uTFYFKJjPtzST0QkX15Jh65wKw0KP-qAL7NT_LLKJbhIXmyvNyLZ9SuhBdT0EWsWIyFE-7HYnv-LN4R-DLieGuHb0rYYCp6lA6bqrtH9N-AcQdzgBRxMWYoWbMZXjBtnOyJb6xnYz-_RYnCWUiQj1a2JgPlHrxf7h9U-ww0K4E64AEw4g3l9TmSLJXbg',
    'Cookie': 'intercom-id-dgkjq2bp=c8fc31d1-5af0-447c-a03b-6f51784e5738; intercom-device-id-dgkjq2bp=0c1eb6da-d512-4750-ac7e-58461cde4f38; oai-did=1ce6f3b4-44a2-454b-aea8-9cc2a4e3675c; ajs_anonymous_id=7f24ca4e-5de9-4ca0-be99-771bc137470a; cf_clearance=Wej2iDZAepeRJKtnXWgbeOm0zvt_lm3ZZca_1UJMcuo-1709915373-1.0.1.1-O8TKQWxfba7BSpb5cvqo_0EGSy58WBxmX8Xm13B1_KvaBL_2BvM_u8WpA6VTYyB3Cboy.ANw6EcMXayohPTEig; __Host-next-auth.csrf-token=f5cb6abeb25687a0d2246e24a4289674c4f01005e9d806b1832c012ed2ac8c21%7C7ccab5694f7987083957dd1be4579a934b8fd2799265bd9fc0ffa2be60a16781; __cf_bm=R58D4knsmpMMUe2o5.2Fw8cVLIRG.MMrv2gBfaIU0lo-1710822071-1.0.1.1-So_gCYjduPrL4x7jdCUW0Ajgxg3TxDUAO_6LmIcVTsmKmAOugajZe3bMa7Vy0_uI7xnWUWEHpuw5K7LwNLjjZw; __cflb=0H28vVfF4aAyg2hkHFTZ1MVfKmWgNcKEvHE6WuVbmaM; _cfuvid=fZ3_WBMMl6_ITP31rxUaW8nwJ0WQYVfuEIw6YA8qNtI-1710822071467-0.0.1.1-604800000; cf_clearance=9TzqnKBsC0lqaNkQGJv2ALmOX68OxpT9Wi0LGkv5ge0-1710822073-1.0.1.1-3_Ia_1bbGReFcK3Q8IO.TH2bUBBt6eMhYGu6TI5kk4C4gN1V9Ax_cY4NiJCuI.iQUjB5EAN6JnOSv3vgR.cc5Q; _uasid="Z0FBQUFBQmwtUk93SnQ2XzFISTZTTVZyaWp4X0tkUDRFMlBYQUxOYkFvZnhxdkh1Q19OWkhmdmFlanJOLTBiY2RLV2N0Ulc2ZGlUXzFzdDdkdTVvVG8zM2w0QTFKMUhCTEF2LVhkQjY1WnJTWkNNTnBHbVhBenNqQkpWR0ZIOVVVUkdFZ2FmNFB5QVl2ZHduTkdsTUs1ZFdvbjA2Tm9jLThOcWw1MHpvR3I1VFYxV0xnTHlDZ3RPYWV0TGpJaTNEMUNIZ2ItczRSTzJLQk1yWHRadU1SaGZ5akZxenpBd0dsVzhaUTZOSEp2WlNtSGVMbzg0MUFZRHBCRTdQZXJzRmlLOTZkWndjZ3F4MF95aFBMbzdoRGpwdDgwV0pVR3ZzOE5GbDdkdlBnLUNWeVFjMno3bTBBRTNxSnBtN3dBQ0dMS3lDVkd2TjVGcEE0U2RKbzhqYzFRV2J3RU1vOGRoOHdBPT0="; _umsid="Z0FBQUFBQmwtUk93bXVrVzhkT25JZ0tVMWlfMXhINGhZT1V3NnhTNUhwWFp3Q0s0X2xwZnFGRk81M3VnZXhCeUJCWFVRRmtwLXVJYWtXa2ZJTjhaMjJIaE5sY0ZVWS0tUWZjYjJpbnpHcGN6MU0tcXBRVEptanRYejRDaThybHlVVEJvbHFBdVpqQ2F3cHdFdEc1WVFKT0dVS2RuS1U1M253Z0JRSExfRXZBd3hyenRWZ1Fyd1pJN2NkNVh1bnFfUkJjLTNEbGlXRmJab2thaVNta0xVaW5razZOR21TU2lQNmJBQmQwU3NkQWFibGxYTm9oODJmMD0="; __Secure-next-auth.callback-url=https%3A%2F%2Fchat.openai.com; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..1KtuIpc4eGKiBBH7.0paNWj0DV69HlB_oohbSmG2VlDyM45KVCIw4WQLp4FE1pGR22srTe4YJepL_EVCp1U4w1lDaxonAb9fH-36ox5JNdKFLlWdNhZpKFOp4IKf2PxRxy2gR2WnBHJXzeUi-9VtGV9KVquD3-R3I096zYM8TDftXObC-TSyWXy4YGfWYj2MN7nBqnPZgt2uYv-GnK1v-DN_8-nkAWeveJORHOKrdQCu1YchvUgpmJUNYy9U8hhK442aldDWabcHrGeP2P_HwnCX6cdytR6XnrkYVtKfdwhEji7nb0bwewAIeFFj-mAfaK6s1sZqizZW1ZdDu4WZPVayJhZUBwpZC828N41bPcmzjL8dvgNERo-dDF1dOcs4NHMo8OAYxgOjXGCk6aih7nMn_AX3wSVgKrBR-dkxw8HYrgp3KAruPE8-7egpbsMfmkBEvH8soSxQf5bmcn34db3fW4_5ezfZE36pclI-dIJL_kBn04P7QzSp3hIpD2_b4IWqm-bxevN5g1a_BU9m25dj4UA5MTsimnkRXkA6-Ad6sdhBLqvOERLbWy0m5n5nEA5N_VK5kK324pPB5tJiK_7VCQto0gtdR7tl_QYHYb8LflucWoTPjRF8KE1hSkLoafKtzPt4DrOh8zJJ22g4GxkPiCUZJpo9KIXD7uJY09qJr8yb7wzwYcNZ-ak5ZIOQ5cPlucxlcLqtdeuPqXAO84iA-pKjnDrMbtqW9KVAlpFJ5-FrD4MisL6tLgZ4ZJM0Skt3llF5FoNsAYwnRszBkeDep4cD7pJWUKcbkyCLYb3vnjdEpdVeofoTVLl3wJ6sATiOjz7oI_4xFgMACFsX0gcLTvTb2VJ2Q9RCOTkX-M1wVghXGP2VPk3r__d0Ff1tlIYD3dyTrNpzZKBKJEyEeNVVpqUG0AFxX0c1K3_xr93GZ3ZKYD-EWo22zPdNYevK6q4qaQDzYCW7BqGVY9h4TJySqtC-SnVACfgXpMY9eqk3URiMqbZsmK0R5tisG4IQBmTO9Wg1oSMdv1dQsgLqsh4b8XT-i7d66JcG2ivEaV4cSGscyV8lmann5DB_FxFaIVMapMFqEUVHPx6uDxkVgjs53YMZlvHFsLqy4IbUFBhzW4PGu3d1Faub1rkamnSyJlzz7il99CgQW1QO2W7MLOVcAU3lYNB-bB11Jmb3yQ0229nQXDJIjvTDuWBzEXC3mGkLH90WvDVb_T8dZliQgHoABLG9t8nfCz5n824aw6Z2q7vOBeOR-zBrnSIpWJoWr7IvU7IiaRTLlKAMvrdU4RIfLC_mMtGc9zcA-75IgTFIM3iKS4yXtZDM3AVPKXNQb4LaJDqaflVZsWQhTw5wg2pHcklsj1rgCPyXsGFFXozDoKsTKBJBzZ3MWsZ5lySJ0cbWBvTzh6vgtcUOXlSWnMa4xYeyq40o8SuWxQxeKiZFhXNEJGkDvU_L69X7-cApns3JQJZA_8mp-SIus-z9SSp9xJb04onmczkEapRTfvvsPZKJxMVtFtjv3snhHJDsmG6n5LkIqXSouS7PiJlg3D4QQmuRhZQS2yeSNOlskQi9yH828iTazfLo0bCJv0xYdJM4wF9E3HEvUGie2FXWcsWRXYVxfD9VylkMpmG7eDpszhHAE95aiRNqBb14vaECgThLcBRuKzaeq1tjJ2Z8yv9aSAV9ot_SHhritY_cbE63iNCuTN_RB_W2bTznWHce7sSJ6mUVQpQJJmUUwdPeUCk7l2TyklhjSxhs16VcOnLCS4jwrwCLpLg63xfoG6-7I0E6LkeqqcgniXJOxHkBpaa_xOU37pTkqju4CnNQCCUVASaLer8Zlf4HSpGcyYnigYo9ZBHvgocA0bx6SKH89uugK8Wo4CCyw_gF746Y75RNzbfdfVzBt5lQREIDlsBVipn6Qe9FnE_7guv86ohuRX-5eDV3DATtX9SrxEQlws7BAaGW3Y2fOypyIa22g8PajtOAslfiT3-k51wLCTueoE8WeIi799jhb-_FMuEUtv5jCkQ2n0NEZJgiYfZIYBHZFGZfJ1Elt3_OnYYxmBM1WOBR7yW2OInZcUc6bgTYG_N4Jq6bjFB7_d3bXM-5HIDWY4ttOAecVl6KLZir276y0mMuMkgm4ON9kgvk3-XD6mD1X_XPNdP0vAJGY6lJhmGYoXBv-w9NqpRLr0YRi5fxKnaNyvisHwGaYkRhJmio1FJj0bg6wIn2FKCdawL8rR6_SkPO62ObDwZoXl7BFyJ4aQXd_DIAobkKa-JJDg1S5bU5SF1HV_fRZn4FzoM3-5YiMj7TH6H4n8XPlSok75Eq5p_dqexuldj9fE6P0pUaGJlAbG6g_71SYyZMO1PWh3yDXXZc8cV0nBY9cdLLwBJbOvzZ_8qTg94qlgIXLf9VrLN5VoiFIyyPNhBUXgQOJ9oV4ImPp0_erMwbLDr-GtJja5iAsmbZFfdya1bH2X4Ae4Zrp5LJW9i4vZBua9y6kt2NJZHyXNMKoRZdaC91xj7wzA7HRWro9RQ3Jpnam_o8SnrNlB62EpL6s9pfJWfvHx_W6n5ple2m81xpyA3MVQ4btdDr-KYjRJu_jIGS0g_RRnjIc2kQwYrsGhw2x1ccC4__tfVPnz0Fp7-D7KyCQenq07HyyiP3cSRkSkcTSPW_v90W11BJV8iYw_D-PGtSGfvdc5qrGSggJSC7xSE1-SZEGHTfKfRdMjAfpPh96ELwZGlvmHC-3Bmfse97Hn1cZGJZxPgW-rWXZhnJIFP1Gl-BKIpi1wqK81prkx0gzedOy5D4.iHaemIcZJEg3RHo7FFXSUA; intercom-session-dgkjq2bp=cW1nQ0VETlFUMUhDdE5zTnIvem9ucXNrY29MWGhQZW03RXlkQXR4ZTNqZ0cwK09GVU43bHd6UEhjRXdhSmFyQS0tNDEzcDhpaUczR1hVU0xnUkVHL1p5QT09--10634e720f0d06e9789074aac8ad8f51cb0d585a; _dd_s=rum=0&expire=1710823581037',
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
