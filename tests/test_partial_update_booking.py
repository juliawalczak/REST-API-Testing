import utilities.methods
from data.testing_data import *

session = utilities.methods.create_session()

def test_create_booking_get_booking_by_id():
    "Given I create a new booking"
    booking_json = BOOKING_1.create_booking_payload()

    response = utilities.methods.create_booking_daria(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I partially update the booking"
    patch_booking_response = utilities.methods.partial_update_booking(ADMIN_USER, session, booking_id, UPDATED_BOOKING_JSON)
    patch_booking_response_json = patch_booking_response.json()

    assert patch_booking_response.status_code == 200
    assert_updated_booking_data(patch_booking_response_json)

    "Then I should still be able to find it on the booking list"
    list_of_bookings_response = utilities.methods.get_all_bookings(session)
    list_of_bookings_response_json = list_of_bookings_response.json()
    list_of_all_values = [value for elem in list_of_bookings_response_json for value in elem.values()]

    assert list_of_bookings_response.status_code == 200
    assert booking_id in list_of_all_values


def test_create_booking_get_all_bookings():
    "Given I create a new booking"
    booking_json = BOOKING_1.create_booking_payload()

    response = utilities.methods.create_booking_daria(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I partially update the booking"
    patch_booking_response = utilities.methods.partial_update_booking(ADMIN_USER, session, booking_id, UPDATED_BOOKING_JSON)
    patch_booking_response_json = patch_booking_response.json()
  
    assert patch_booking_response.status_code == 200
    assert_updated_booking_data(patch_booking_response_json)

    "Then I should get updated booking data by ID"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert_updated_booking_data(get_booking_response_json)


def assert_updated_booking_data(response_body):
        assert response_body['firstname'] == "Harry"
        assert response_body['lastname'] == "Malfoy"
        assert response_body['totalprice'] == 999
        assert response_body['depositpaid'] == False
        assert response_body['bookingdates']['checkin'] == '2022-10-01'
        assert response_body['bookingdates']['checkout'] == '2022-10-22'
        assert response_body['additionalneeds'] == 'Dinner'
