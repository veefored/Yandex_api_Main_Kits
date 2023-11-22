import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body,headers=data.headers)
def post_new_client_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, json=kit,headers=data.headers)
    response = post_kit_body(data.kit_body);
    response = post_new_client_kit(body);
print (response.status_code)
print (response.json())