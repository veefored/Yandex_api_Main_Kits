import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
def post_new_client_kit(body):
    return requests.post(kit_body.auth_token)
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())