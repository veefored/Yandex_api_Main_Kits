import configuration
import requests
import data

# Добавление нового пользователя
def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

response = post_new_user (data.user_body);

# Получение токена нового пользователя
def get_new_user_authToken (body):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH)

# Сохранение токена

data.authToken["Autrization"] = str(response.json())

# Добавление набора текущего пользователя
def post_new_client_kit (body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         headers=data.authToken, json=body)

