import sender_stand_request


# Проверяется, что код ответа равен 201
assert user_response.status_code == 201
# Проверяется, что в ответе есть поле authToken, и оно не пустое
assert user_response.json()["authToken"] != ""