import datetime
import vk_api
import random
from config import token

#создаем сессию

vk = vk_api.VkApi(token=token)
#авторизуем токен
vk._auth_token()
#проверка на сервере вк приходящие сообщения

# print(messages)
#print(datetime.datetime.now().time())
try:
    while True:
        now = datetime.datetime.now().time()
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            text = messages["items"][0]["last_message"]["text"]
            user_id = messages["items"][0]["last_message"]["from_id"]
            if text.lower() == 'привет':
                vk.method("messages.send", {"user_id": user_id, "message": "Привет", "random_id": random.randint(1, 10000)})
            else:
                vk.method("messages.send", {"user_id": user_id, "message": "Привет, я тупой бот, ничего не понимаю", "random_id": random.randint(1, 10000)})

except vk_api.exceptions.ApiError:
    print("Something wrong!")


