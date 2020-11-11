# -*- coding: utf-8 -*-
from logic import VkEventType, longpoll, send_message, create_new_list, show_lists


CREATE = '/create'
ADD = '/add'
DELETE = '/delete'
UPDATE = '/update'
HELP = '/help'
COMANDS = (
    CREATE,
    ADD,
    DELETE,
    HELP
)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        message = event.text.lower()
        user_id = event.user_id

        if event.to_me:
            if message == '/create':
                send_message(user_id, 'Создаем твой список)\nНапиши, как ты его назовешь')
                if not create_new_list(user_id):
                    send_message(user_id, 'Ох( Такой список уже есть\nСоздай его заново!')
                else:
                    send_message(user_id, 'Успешна)\nСписок создан')
            elif message == '/show':
                if not show_lists(user_id):
                    send_message(user_id, 'Похоже у тебя нет ни одного списка(\nСоздай! (/create)')
                else:
                    send_message(user_id, 'Вот все списки что у тебя есть:')
                    send_message(user_id, '\n'.join(show_lists(user_id)))
            elif message == '/help':
                send_message(user_id, f"Этот бот создает списки для тебя и ты их форматируешь)\nВот команды, котрые ты можешь использовать: {', '.join(COMANDS)}")

            # elif message == '/add':s
            #     send_message(user_id, 'Выбери список, в который ты хочешь добавить записи:')
            #     # put_in_list(user_id)
            # else:
            #     send_message(user_id, "Не понимаю тебя(\nВот команды которые я знаю:\n")
            #     send_message(user_id, '/create\n/add\n/delete\n/update\n/show')
