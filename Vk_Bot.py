import os
import sys
import time
import vk_api
import vk as api

from vkplus import VkPlus

import settings

vk = VkPlus(settings.vk_login, settings.vk_password, settings.vk_app_id)

def main():
    path = 'plugins/'
    cmds = {}
    plugins = {}

    global lastmessid
    lastmessid = 0
    global vk

    print('Vk_Bot by Adventurous Community')

    print('Авторизация...')

    vk = VkPlus(settings.vk_login, settings.vk_password, settings.vk_app_id)

    print('Приступаю к приему сообщений')

    while True:

        values = {
            'out': 0,
            'offset': 0,
            'count': 20,
            'time_offset': 50,
            'filters': 0,
            'preview_length': 0,
            'last_message_id': lastmessid
        }

        response = vk.api.method('messages.get', values)
        if response['items']:
            lastmessid = response['items'][0]['id']
            for item in response['items']:
                print('> ' + item['body'])
                command(item, cmds)
                vk.markasread(item['id'])  # Помечаем прочитанным

        time.sleep(0.5)


def command(message, cmds):
    if message['body'] == u'':
        return
    global vk
    for word in message['body'].split():
        if len(word) >= 3 and (word.lower() in 'хербляяя' or word.lower() in 'блядинаблядь' or word.lower() in 'ебатьпиздецхуйхуихуйло' or word.lower() in 'блядиадаблядскийблять' or word.lower() in 'сукапидоруёбокуебанпидрилапиздапроёбинамудак') and message['chat_id'] == 99:
            vk.send('Бан 300 лет!', 'photo255888582_456239600')
            time.sleep(1)
            vk.remove_user(message['user_id'])
            time.sleep(432000)
            vk.add_user(message['user_id'])
            break



if __name__ == '__main__':
    main()