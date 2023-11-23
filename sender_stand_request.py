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
def get_new_user_authToken (body):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=authToken)

print (data.authToken)
def post_new_client_kit (body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         params=data.kit_body,
                         headers=data.authToken,
                         json=data.kit_body)

response = post_new_client_kit(data.kit_body)

print (response.status_code)
print (response.json())
