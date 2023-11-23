import sender_stand_request
import data


# эта функция меняет значения в параметре firstName
def get_new_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["Name"] = name

    return current_kit_body


# Тест 1. Параметр kit_Name состоит из 1 символа
def test_create_kit_name_1_letter_in_name_get_success_response():
    kit_body = get_new_kit_body("a")
    kit_response = sender_stand_request.kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]
