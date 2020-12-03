import vk_api
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType
from secret import main_token

vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_message(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            user_id = event.user_id
            send_message(user_id,
                         'Привет!\nЭтот бот помагает состоявлять, обновлять и удалять списки.\nВот следующие команды, '
                         'котрые ты можешь использовать:')
