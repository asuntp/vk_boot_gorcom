import vk_api
from random import randint
from config import token

#создаем сессию

vk = vk_api.VkApi(token=token)
#авторизуем токен
vk._auth_token()

#проверка на сервере вк приходящие сообщения
try:
    while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered "})
        if messages["count"]>=1:
            text = messages["items"][0]["last_message"]["text"]
            user_id = messages["items"][0]["last_message"]["from_id"]
            if text.lower() == str:
                vk.method("message.send", {"user_id": user_id, "message": "Привет",
                                           "random_id": randint(1, 1000)})
            else:
                vk.method("message.send", {"user_id": user_id, "message": "Привет, я бот, ничего не понимаю",
                                       "random_id": randint(1, 1000)})
        else:
            continue




