from collections import OrderedDict
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def read_auth():
    with open('authorization.txt', 'r', encoding='utf-8') as file:
        auth = file.read()
    return auth
    

# 发送提示词 , 提示词，种子，文件，负面关键词，纵横比，是否开启配音
def send_keys(prompt, seed, files, word, ap, sfx):
    if sfx:
        sfx = 'true'
    else:
        sfx = 'false'
    search = prompt
    params = OrderedDict([
        ("sfx", (None, sfx)),
        ("promptText", (None, f'{search}', 'multipart/form-data'))
        , ("options", (None, '{"aspectRatio":' + str(ap) +
                       ',"frameRate":24,"camera":{},"parameters":{'
                       '"guidanceScale":12,"motion":3,"negativePrompt":"' + str(word) + '","seed":' + str(
            seed) + '},"extend":"false" }'))
        , ("userId", (None, 'ba12fbbb-907a-443b-9c39-939c73bedfc6')),
    ])
    if files:
        try:
            params['image'] = ('image', files, 'image/jpg')
        except Exception as e:
            print('e:' + str(e))

    multipart_data = MultipartEncoder(params)
    url_generate = 'https://api.pika.art/generate'
    res = requests.post(url_generate, data=multipart_data,
                        headers={'Content-Type': multipart_data.content_type,
                                 'Authorization': read_auth()
                                 })
    return res
