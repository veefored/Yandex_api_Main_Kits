import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name

    return current_kit_body

# Тест 1. Параметр kit_Name состоит из Допустимое количество символов (1)
def test_positive_assert_create_new_kit_name_1_letter_in_name_post_success_response():
    kit_body = get_kit_body("a")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 2. Параметр kit_Name состоит из Допустимое количество символов (511)
def test_positive_assert_create_new_kit_name_511_letter_in_name_post_success_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 3. Параметр kit_Name состоит из Количество символов меньше допустимого (0)
def test_negative_assert_create_new_kit_name_empty_letter_in_name_post_error_response():
    kit_body = get_kit_body("")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 4. Параметр kit_Name состоит из Количество символов больше допустимого (512)
def test_negative_assert_create_new_kit_name_512_letter_in_name_post_error_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabCA")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 5. Параметр kit_Name состоит из Разрешены английские буквы: "QWErty"
def test_positive_assert_create_new_kit_name_english_letter_in_name_post_success_response():
    kit_body = get_kit_body("QWErty")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 6. Параметр kit_Name состоит из Разрешены русские буквы: "Мария"
def test_positive_assert_create_new_kit_name_russian_letter_in_name_post_success_response():
    kit_body = get_kit_body("Мария")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 7. Параметр kit_Name состоит из Разрешены спецсимволы: "№%@"
def test_positive_assert_create_new_kit_name_special_symbol_letter_in_name_post_success_response():
    kit_body = get_kit_body("№%@")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 8. Параметр kit_Name состоит из Разрешены пробелы: "Человек и КО"
def test_positive_assert_create_new_kit_name_has_space_letter_in_name_post_success_response():
    kit_body = get_kit_body("Человек и КО")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 9. Параметр kit_Name состоит из Разрешены цифры: 123
def test_positive_assert_create_new_kit_name_number_type_letter_in_name_post_success_response():
    kit_body = get_kit_body("123")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 10. Параметр kit_Name состоит из Параметр не передан в запросе:
def test_negative_assert_create_new_kit_name_no_letter_in_name_post_error_response():
    kit_body = get_kit_body("message")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 11. Параметр kit_Name состоит из Передан другой тип параметра (число): 123
def test_negative_assert_create_new_kit_name_number_type_letter_in_name_post_success_response():
    kit_body = get_kit_body(123)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]
