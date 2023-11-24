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
    kit_response = sender_stand_request.post_new_client_kit("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabC")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 3. Параметр kit_Name состоит из Количество символов меньше допустимого (0)

def test_create_new_kit_name_0_letter_in_name_post_error_response():
    kit_body = post_new_kit_body("")
    kit_response = sender_stand_request.post_new_client_kit("")

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 4. Параметр kit_Name состоит из Количество символов больше допустимого (512)

def test_create_new_kit_name_512_letter_in_name_post_error_response():
    kit_body = post_new_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabCA")
    kit_response = sender_stand_request.post_new_client_kit("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabCA")

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 5. Параметр kit_Name состоит из Разрешены английские буквы: "QWErty"
def test_create_new_kit_name_QWErty_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("QWErty")
    kit_response = sender_stand_request.post_new_client_kit("QWErty")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 6. Параметр kit_Name состоит из Разрешены русские буквы: "Мария"
def test_create_new_kit_name_Мария_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("Мария")
    kit_response = sender_stand_request.post_new_client_kit("Мария")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 7. Параметр kit_Name состоит из Разрешены спецсимволы: "№%@"
def test_create_new_kit_name_1_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("№%@")
    kit_response = sender_stand_request.post_new_client_kit("№%@")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 8. Параметр kit_Name состоит из Разрешены пробелы: "Человек и КО"
def test_create_new_kit_name_Человек_и_КО_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("Человек и КО")
    kit_response = sender_stand_request.post_new_client_kit("Человек и КО")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 9. Параметр kit_Name состоит из Разрешены цифры: "123"
def test_create_new_kit_name_123_letter_in_name_post_success_response():
    kit_body = post_new_kit_body("123")
    kit_response = sender_stand_request.post_new_client_kit("123")

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 10. Параметр kit_Name состоит из Параметр не передан в запросе: ""
def test_create_new_kit_name_letter_in_name_post_error_response():
    kit_body = post_new_kit_body("")
    kit_response = sender_stand_request.post_new_client_kit("")

    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == kit_body["name"]

