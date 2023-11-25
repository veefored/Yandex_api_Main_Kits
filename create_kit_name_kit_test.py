import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name

    return current_kit_body

# Тест 1. Параметр kit_Name состоит из Допустимое количество символов (1)
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_1_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("a")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 2. Параметр kit_Name состоит из Допустимое количество символов (511)
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_511_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabC")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 3. Параметр kit_Name состоит из Количество символов меньше допустимого (0)
# Функция для негативной проверки
def test_negative_assert_create_new_kit_name_empty_letter_in_name_post_error_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 400
    assert kit_response.status_code == 400
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 4. Параметр kit_Name состоит из Количество символов больше допустимого (512)
# Функция для негативной проверки
def test_negative_assert_create_new_kit_name_512_letter_in_name_post_error_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabCA")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 400
    assert kit_response.status_code == 400
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 5. Параметр kit_Name состоит из Разрешены английские буквы: "QWErty"
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_english_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("QWErty")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 6. Параметр kit_Name состоит из Разрешены русские буквы: "Мария"
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_russian_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("Мария")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 7. Параметр kit_Name состоит из Разрешены спецсимволы: "№%@"
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_special_symbol_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("№%@")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 8. Параметр kit_Name состоит из Разрешены пробелы: "Человек и КО"
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_has_space_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("Человек и КО")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 9. Параметр kit_Name состоит из Разрешены цифры: 123
# Функция для позитивной проверки
def test_positive_assert_create_new_kit_name_number_type_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("123")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 201
    assert kit_response.status_code == 201
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]

# Тест 10. Параметр kit_Name состоит из Параметр не передан в запросе:
# Функция для негативной проверки
def test_negative_assert_create_new_kit_name_no_letter_in_name_post_error_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body("message")
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 400
    assert kit_response.status_code == 400
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]
# проверяется, что в ответе получаем сообщение "Не все необходимые параметры были переданы"
    assert kit_response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 11. Параметр kit_Name состоит из Передан другой тип параметра (число): 123
# Функция для негативной проверки
def test_negative_assert_create_new_kit_name_number_type_letter_in_name_post_success_response():
# в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(123)
# в переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
# проверяется, что код ответа соответствует коду 400
    assert kit_response.status_code == 400
# проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]
