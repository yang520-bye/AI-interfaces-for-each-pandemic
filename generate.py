import base64
import random
from collections import OrderedDict
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder

Authorization = '你账号的Authorization'

# base64转图片
def base64_to_image(base64_string, output_file):
    try:
        base64_data = re.sub('^data:image/.+;base64,', '', base64_string)
        image_data = base64.b64decode(base64_data)
        with open(output_file, 'wb') as f:
            f.write(image_data)
    except Exception as e:
        print("转换出错:", e)


# 发送提示词
def send_keys(prompt, seed, files, word, ap, sfx):
    print('send')
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
            print('e' + str(e))

    multipart_data = MultipartEncoder(params)
    # print(multipart_data)
    url_generate = 'https://api.pika.art/generate'
    res = requests.post(url_generate, data=multipart_data,
                        headers={'Content-Type': multipart_data.content_type,
                                 'Authorization': Authorization
                                 })
    return res
