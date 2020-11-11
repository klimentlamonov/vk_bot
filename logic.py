# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from secret import main_token
import file_logic


""" Globals.

Starting session and create key words.
"""

lists = dict()
vk_session = vk_api.VkApi(token = main_token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


""" Functions.

For working with VK.
"""

def send_message(id, text):
    vk.messages.send(user_id = id, message = text, random_id = 0)


def create_new_list(user_id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                lst_name = event.text
                user_id = event.user_id
                if not file_logic.create_new_list(user_id, lst_name):
                    return False
                return True


def show_lists(user_id):
    return file_logic.show_my_lists(user_id)


# def put_in_list(user_id):
#     show_lists(user_id)
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW:
#             if event.to_me:
#                 lst_name = event.text
#                 user_id = event.user_id
#                 lists[lst_name] = []
#                 send_message(user_id, f'Товой список {lst_name} создан!')
#                 return True