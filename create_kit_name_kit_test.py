import sender_stand_request
import data
def post_new_kit_name(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["Name"] = name

    return current_kit_body
def positive_assert(name):
    kit_body = post_new_kit(name)
    create_kit_response = sender_stand_request.post_new_kit(name)

    assert create_kit_response.status_code == 201
    assert create_kit_response.json()["name"] == kit_body["name"]

# Тест 1. Успешное создание пользователя. Параметр kit_Name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")