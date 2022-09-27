import utilities.methods
from data.testing_data import *
import pytest

session = utilities.methods.create_session()

@pytest.mark.parametrize("booker", bookers)
def test_create_booking_get_booking_by_id(booker):
    "Given I create a new booking"
    booking_json = booker.create_booking_payload()

    response = utilities.methods.create_booking_daria(booker, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I get the booking by ID"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    get_booking_response_response = get_booking_response.json()

    "Then I successfully get new booking data"
    assert get_booking_response.status_code == 200
    assert get_booking_response_response == booking_json


@pytest.mark.parametrize("booker", bookers)
def test_create_booking_get_all_bookings(booker):
    "Given I create a new booking"
    booking_json = booker.create_booking_payload()

    response = utilities.methods.create_booking_daria(booker, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I get all bookings list"
    bookings_response = utilities.methods.get_all_bookings(session)
    bookings_response_body = bookings_response.json()
    booking_ids = [value for elem in bookings_response_body for value in elem.values()]

    "Then I successfully get new booking data"
    assert bookings_response.status_code == 200
    assert booking_id in booking_ids
