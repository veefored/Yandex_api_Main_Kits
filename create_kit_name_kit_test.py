import sender_stand_request
import data

def post_new_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["Name"] = name

    return current_kit_body

# Тест 1. Параметр kit_Name состоит из 1 символа
def test_create_new_kit_name_1_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("a")
    kit_response = sender_stand_request.post_new_client_kit("a")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 2. Параметр kit_Name состоит из Допустимое количество символов (511)
def test_create_new_kit_name_511_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_client_kit("a")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 3. Параметр kit_Name состоит из Количество символов меньше допустимого (0)

def test_create_new_kit_name_0_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("")
    kit_response = sender_stand_request.post_new_client_kit("")

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

