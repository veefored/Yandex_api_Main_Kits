import sender_stand_request
import data
def post_new_kit(name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["firstName"] = name

    return current_kit_name
def positive_assert(name):
    kit_body = post_new_kit(name)
    create_kit_response = sender_stand_request.post_new_kit()

    assert create_kit_response.status_code == 201
    assert kit_response.json()["authToken"] != ""

# Тест 1. Успешное создание пользователя. Параметр kit_Name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")