import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from secret import main_token

vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_message(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
