import utilities.booking_methods
from data.testing_data import *

session = utilities.booking_methods.create_session()

def test_create_booking_get_booking_by_id():
    "Given I create a new booking"
    booking_json = BOOKING_1.to_json()

    response = utilities.booking_methods.create_booking(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I partially update the booking"
    patch_booking_response = utilities.booking_methods.partial_update_booking(ADMIN_USER, session, booking_id, UPDATED_BOOKING_JSON)
    patch_booking_body = patch_booking_response.json()

    assert patch_booking_response.status_code == 200
    assert_updated_booking_data(patch_booking_body)

    "Then I should still be able to find it on the booking list"
    get_bookings_response = utilities.booking_methods.get_all_bookings(session)
    get_bookings_body = get_bookings_response.json()
    booking_ids = [value for elem in get_bookings_body for value in elem.values()]

    assert get_bookings_response.status_code == 200
    assert booking_id in booking_ids


def test_create_booking_get_all_bookings():
    "Given I create a new booking"
    booking_json = BOOKING_1.to_json()

    response = utilities.booking_methods.create_booking(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I partially update the booking"
    patch_booking_response = utilities.booking_methods.partial_update_booking(ADMIN_USER, session, booking_id, UPDATED_BOOKING_JSON)
    patch_booking_body = patch_booking_response.json()

    assert patch_booking_response.status_code == 200
    assert_updated_booking_data(patch_booking_body)

    "Then I should get updated booking data by ID"
    get_booking_response = utilities.booking_methods.get_booking_by_id(booking_id, session)
    get_bookings_body = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert_updated_booking_data(get_bookings_body)


def assert_updated_booking_data(response_body):
        assert response_body['firstname'] == "Harry"
        assert response_body['lastname'] == "Malfoy"
        assert response_body['totalprice'] == 999
        assert response_body['depositpaid'] == False
        assert response_body['bookingdates']['checkin'] == '2022-10-01'
        assert response_body['bookingdates']['checkout'] == '2022-10-22'
        assert response_body['additionalneeds'] == 'Dinner'
