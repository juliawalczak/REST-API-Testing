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

    "When I update booking"
    updated_booking_json = BOOKING_2.create_booking_payload()
    update_response = utilities.methods.update_booking(ADMIN_USER, session, booking_id, BOOKING_2)

    assert update_response.status_code == 200
    assert update_response.json() == updated_booking_json

    "Then I should get updated booking data by ID"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    get_booking_response_response = get_booking_response.json()

    "Then I successfully get new booking data"
    assert get_booking_response.status_code == 200
    assert get_booking_response_response == updated_booking_json


def test_create_booking_get_all_bookings():
    "Given I create a new booking"
    booking_json = BOOKING_1.create_booking_payload()

    response = utilities.methods.create_booking_daria(BOOKING_1, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I update booking"
    update_response = utilities.methods.update_booking(ADMIN_USER, session, booking_id, BOOKING_2)

    assert update_response.status_code == 200
    assert update_response.json() == BOOKING_2.create_booking_payload()

    "Then I should still be able to find it on the booking list"
    bookings_response = utilities.methods.get_all_bookings(session)
    bookings_response_body = bookings_response.json()
    booking_ids = [value for elem in bookings_response_body for value in elem.values()]

    assert bookings_response.status_code == 200
    assert booking_id in booking_ids
