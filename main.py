# -*- coding: utf-8 -*-
from logic import *


CREATE = 'создать'
ADD = 'добавить'
DELETE = 'удалить'
UPDATE = 'обновить'
HELP = 'помоги'
SHOW = 'покажи'
COMANDS = (
    CREATE,
    ADD,
    DELETE,
    HELP,
    SHOW
)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        message = event.text.lower()
        user_id = event.user_id

        if event.to_me:
            if message == CREATE:
                send_message(user_id, 'Создаем твой список)\nНапиши, как ты его назовешь')
                if not create_new_list(user_id):
                    send_message(user_id, 'Ох( Такой список уже есть\nСоздай его заново!')
                else:
                    send_message(user_id, 'Успешна)\nСписок создан')
            elif message == SHOW:
                if not show_lists(user_id):
                    send_message(user_id, 'Похоже у тебя нет ни одного списка(\nСоздай!')
                else:
                    send_message(user_id, 'Вот все списки что у тебя есть:')
                    send_message(user_id, '\n'.join(show_lists(user_id)))
            elif message == HELP:
                send_message(user_id, f"Этот бот создает списки для тебя и ты их форматируешь)\nВот команды, котрые ты можешь использовать:\n{', '.join(COMANDS).title()}")
            elif message == DELETE:
                send_message(user_id, "Оки, отправь мне имя списка, от которого хочешь избавиться.\nВот списки, которые у тебя есть ")
                send_message(user_id, '\n'.join(show_lists(user_id)))
                if not delete_list(user_id):
                    send_message(user_id, 'Огог\nНе получилось удалить(')
                else:
                    send_message(user_id, 'Список удален')
            elif message == ADD:
                send_message(user_id, "Оки доки, добавлю записи в твой список.\nВведи название списка, а затем через запятую введи строки, которые хочешь внести в список\nТакого типа: \"Мой список, Запись 1, Запись 2\"")
                send_message(user_id, '\n'.join(show_lists(user_id)))
                if not add_to_list(user_id):
                    send_message(user_id, "Что-то явно пошло не так(\nНе получилось добавить. Проверь, а ты правильно все написал?")
                else:
                    send_message(user_id, "Твои записи в списке!")
            else:
                send_message(user_id, f"Что-то на эльфийском, не могу прочесть(\nВот команды, которые я понимаю:\n{', '.join(COMANDS).title()}")
