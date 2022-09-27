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

    "When I update booking"
    updated_booking_json = BOOKING_2.to_json()
    update_response = utilities.booking_methods.update_booking(ADMIN_USER, session, booking_id, BOOKING_2)

    assert update_response.status_code == 200
    assert update_response.json() == updated_booking_json

    "Then I should get updated booking data by ID"
    get_booking_response = utilities.booking_methods.get_booking_by_id(booking_id, session)
    get_booking_body = get_booking_response.json()

    "Then I successfully get new booking data"
    assert get_booking_response.status_code == 200
    assert get_booking_body == updated_booking_json


def test_create_booking_get_all_bookings():
    "Given I create a new booking"
    booking_json = BOOKING_1.to_json()

    response = utilities.booking_methods.create_booking(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I update booking"
    update_response = utilities.booking_methods.update_booking(ADMIN_USER, session, booking_id, BOOKING_2)

    assert update_response.status_code == 200
    assert update_response.json() == BOOKING_2.to_json()

    "Then I should still be able to find it on the booking list"
    get_bookings_response = utilities.booking_methods.get_all_bookings(session)
    get_bookings_body = get_bookings_response.json()
    booking_ids = [value for elem in get_bookings_body for value in elem.values()]

    assert get_bookings_response.status_code == 200
    assert booking_id in booking_ids
