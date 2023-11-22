import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
def post_new_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=body,
                         headers=data.headers)
str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
response = post_new_user(data.user_body);
print(response.status_code)
