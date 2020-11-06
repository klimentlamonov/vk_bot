import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from secret import main_token

""" Globals.

Starting session and create key words.
"""

START = '/start'
ADD = '/add'
DELETE = '/delete'
UPDATE = '/update'
lists = dict()
vk_session = vk_api.VkApi(token = main_token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_message(id, text):
    vk.messages.send(user_id = id, message = text, random_id = 0)


def create_new_list(user_id):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                lst_name = event.text
                user_id = event.user_id
                lists[lst_name] = []
                send_message(user_id, f'Товой список "{lst_name}" создан!')
                return True


def show_lists(user_id):
    for k, v in lists.items():
        if lists[k] == []:
            send_message(user_id, f'Пустой список "{k}"')
        else:
            send_message(user_id, f'Список "{k}" со содержимым: {i for i in v}')
    return True


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


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        message = event.text.lower()
        user_id = event.user_id

        if event.to_me:
            if message == '/start':
                send_message(user_id, 'Создаем твой список)\nНапиши, как ты его назавешь')
                create_new_list(user_id)
            elif message == '/show':
                send_message(user_id, 'Вот все списки что у тебя есть:')
                show_lists(user_id)
            elif message == '/add':
                send_message(user_id, 'Выбери список, в который ты хочешь добавить записи:')
                # put_in_list(user_id)
            else:
                send_message(user_id, "Не понимаю тебя(\nВот команды которые я знаю:\n")
                send_message(user_id, '/start\n/add\n/delete\n/update\n/show')
