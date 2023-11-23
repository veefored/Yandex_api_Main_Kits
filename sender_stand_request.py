import configuration
import requests
import data
def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

response = post_new_user (data.user_body);

print (response.status_code)
print (response.json())
def get_new_user_authToken():
    return requests.get(data.authToken, json=data.authToken)
data.get_new_user_authToken["Autorization"]
print (data.authToken)
def post_new_client_kit (body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=data.kit_body,
                         headers=data.headers)

response = post_new_client_kit(data.kit_body)
print (response.status_code)
print (response.json())
