import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body,headers=data.headers)
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + )
def get_new_user_token():
    response = post_new_user(data.user_body)
    response = post_new_client_kit(body)
print(response.status_code)
print(response.json())