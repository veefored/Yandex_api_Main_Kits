import configuration
import requests
import data
def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user (data.user_body);

print (response.status_code)
print (response.json())

data.headers_authToken ["Authorization"] = response.json()
print (data.headers_authToken)
def post_new_kit (body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_kit(data.kit_body)
print (response.status_code)
print (response.json())
