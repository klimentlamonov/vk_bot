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
                
                # return file_logic.create_new_list(user_id, lst_name) if not 
                # сделать так, чтобы каждый лист назывался УНИКАЛЬНО!


def show_lists(user_id):
    lsts = dict()
    try:
        for lst in file_logic.show_my_lists(user_id):
            lsts[lst] = file_logic.read_list(user_id, lst)
        return lsts
    except Exception:
        return None


def show_all_lists(user_id):
    pass


def delete_list(user_id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                lst_name = event.text
                user_id = event.user_id

                file_logic.delete_list(user_id, lst_name)
                if lst_name in show_lists(user_id):
                    return False
                return True


def add_to_list(user_id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                lst_and_fields = event.text.split(", ")
                user_id = event.user_id

                if len(lst_and_fields) < 1:
                    return False 
                try:
                    current_list = file_logic.read_list(user_id, lst_and_fields[0]) + lst_and_fields[1:]
                    file_logic.write_in_list(user_id, lst_and_fields[0], current_list)
                    return True
                except Exception:
                    return False
