# -*- coding: utf-8 -*
'''
2 10 * * * smzdm_sign.py
new Env('什么值得买签到');
'''
import requests
import json
import time
import hashlib
import os

def gettoken(ck):
    ts = time.time() * 1000
    url = 'https://user-api.smzdm.com/robot/token'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{ck}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    data = {
        "f": "android",
        "v": "10.4.1",
        "weixin": 1,
        "time": ts,
        "sign": hashlib.md5(bytes(f'f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC', encoding='utf-8')).hexdigest().upper()
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = html.json()
    return result['data']['token']


def sign(ck):
    ts = time.time() * 1000
    token = gettoken(ck)
    data = {
        "f": "android",
        "v": "10.4.1",
        "sk": "ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
        "weixin": 1,
        "time": ts,
        # "token":"NcvkeyVy82Qqg3T9oHLTquZr2j3XG%2FSgc7HEfiG08bRHv6qht1gG69tk2mp5rQtVZiTiJB348l9AIOmjsNVq",
        "token": token,
        "sign": hashlib.md5(bytes(f'f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={ts}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC', encoding='utf-8')).hexdigest().upper()
    }
    url = 'https://user-api.smzdm.com/checkin'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{ck}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = json.loads(html.text)
    # print(result)
    print(result['error_msg'])
    print('已连续签到'+result['data']['daily_num']+'天')


def reward(ck):
    ts = time.time() * 1000
    data = {
        "f": "android",
        "v": "10.4.1",
        "weixin": 1,
        "time": ts,
        "sign": hashlib.md5(bytes(f'f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC', encoding='utf-8')).hexdigest().upper()
    }
    url = 'https://user-api.smzdm.com/checkin/all_reward'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{ck}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    html = requests.post(url=url, headers=headers, data=data)


    # result = json.loads(html.text)
if __name__ == '__main__':
    ck = [
        #这里填入cookie，"XXXXX"
    ]
    if os.environ["ZDMCK"]:
        ck=os.environ["ZDMCK"].split("&")

    for i in ck:
        sign(i)
        time.sleep(1)
        reward(i)
