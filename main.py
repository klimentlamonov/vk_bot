from logic import *


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            user_id = event.user_id
            send_message(user_id,
                         'Привет!\nЭтот бот помагает состоявлять, обновлять и удалять списки.\nВот следующие команды, '
                         'котрые ты можешь использовать:')
