import configuration
import requests
import data
def get_new_user_token():
    return post_new_user(data.user_body).json()["auth_token"]

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers={"Authorization": "Bearer {auth_token}" + get_new_user_token()
 })

response = post_new_client_kit(data.kit_body, auth_token)
print(response.status_code)
print(response.json())
