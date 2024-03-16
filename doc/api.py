import json
import random
import re
import time
import requests
from bs4 import BeautifulSoup

from pika.generate import send_keys


def read_cookie():
    with open('cookie.txt', 'r', encoding='utf-8') as file:
        cookie = file.read()
    return cookie


header = {
    'Cookie': read_cookie()
}


def has_mp4_resource(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1_tag = soup.find('video')
    return h1_tag


# 本地存储
def LocalStorage(generation_id, prompt, url, jpg):
    cs = 'http://localhost:8081/static/'
    response = requests.get(url, stream=True)
    jpgs = cs + str(generation_id) + '.jpg'
    urls = cs + str(generation_id) + '.mp4'

    with open('static/' + str(generation_id) + '.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    response = requests.get(jpg)
    with open('static/' + str(generation_id) + '.jpg', 'wb') as file:
        file.write(response.content)
    return {'prompt': prompt, 'jpg': jpgs, 'url': urls}


def process_request(generation_id, prompt, url, jpg):
    time.sleep(30)
    while True:
        time.sleep(6)
        has_mp4 = has_mp4_resource(requests.get(f'https://pika.art/video/{generation_id}', headers=header).text)
        if has_mp4:
            item = LocalStorage(generation_id, prompt, url, jpg)
            return item


# 发送提示词 , 提示词，种子，文件，负面关键词，纵横比，是否开启配音 , 返回本地资源
def send(prompt, seed=random.seed, files=None, bad_word='ugly bad', ap=1.7777777777777777, sfx=False):
    r = send_keys(prompt, seed, files, bad_word, ap, sfx)
    response_data = json.loads(r.text)
    generation_id = response_data['data']['generation']['id']
    content = re.sub(r'[\u4e00-\u9fff\s]', '_', prompt[:101])
    url_jpg = f'https://cdn.pika.art/v1/{generation_id}/poster.jpg'
    mp4_link = f'https://cdn.pika.art/v1/{generation_id}/{content}_seed{seed}.mp4'
    item = process_request(generation_id, prompt, mp4_link, url_jpg)
    return item
