import sender_stand_request
import data
def post_new_kit(name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["firstName"] = name

    return current_kit_name
def positive_assert(name):
    kit_body = post_new_kit(name)
    kit_response = sender_stand_request.post_new_kit()

    assert kit_response.status_code == 201
    assert kit_response.json()["authToken"] != ""
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")