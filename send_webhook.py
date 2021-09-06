import os
from datetime import datetime
import requests
import json


def configure_data(island_data):
    now_time = datetime.now()

    embed_field_list = [i.__dict__ for i in island_data]

    day = ['월', '화', '수', '목', '금', '토', '일']
    title = now_time.strftime("%Y/%m/%d") + f" ({day[now_time.weekday()]})"
    if now_time.weekday() not in [5, 6]:
        appear_time_string = "11, 13, 19, 21, 23시"
    else:
        if now_time.hour <= 13:
            title += " 오전"
            appear_time_string = "9, 11, 13시"
        else:
            title += " 오후"
            appear_time_string = "19, 21, 23시"

    embed_data = {
        'author': {
            'name': "모험섬 정보",
            'url': os.getenv('DATA_SOURCE')
        },
        'title': title,
        'description': f'출현 시간: {appear_time_string}',
        'color': 14177041,
        'fields': embed_field_list,
        'footer': {
            'text': now_time.strftime("%Y-%m-%d %H:%M") + " 기준"
        }
    }

    post_data = {
        'username': os.getenv("WEBHOOK_USERNAME"),
        'avatar_url': os.getenv('WEBHOOK_AVATAR_URL'),
        'embeds': [embed_data]
    }

    return post_data


def send_webhook(island_data):
    post_data = configure_data(island_data)

    header = {
        'Content-Type': 'application/json'
    }

    for i in configure_txt_file_to_list():
        requests.post(url=i, data=json.dumps(post_data), headers=header)


def configure_txt_file_to_list():
    data = []
    with open('webhook_list.txt', 'r', encoding='UTF8') as f_in:
        for line in f_in:
            line = line.split('#', maxsplit=1)[0].strip()
            if line:
                data.append(line)

    return data

