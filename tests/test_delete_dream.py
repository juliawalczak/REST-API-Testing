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

    "When I delete booking"
    delete_booking_response = utilities.methods.delete_booking(ADMIN_USER, session, booking_id)
    assert delete_booking_response.status_code == 201

    "Then I should't see the booking in all bookings list"
    bookings_response = utilities.methods.get_all_bookings(session)
    bookings_body = bookings_response.json()
    booking_id = [value for elem in bookings_body for value in elem.values()]

    assert bookings_response.status_code == 200
    assert booking_id not in booking_id


@pytest.mark.parametrize("booker", bookers)
def test_create_booking_get_all_bookings(booker):
    "Given I create a new booking"
    booking_json = booker.create_booking_payload()

    response = utilities.methods.create_booking_daria(booker, session)
    response_body = response.json()
    booking_id = response_body['bookingid']

    assert response.status_code == 200
    assert response_body['booking'] == booking_json

    "When I delete the booking"
    delete_booking_response = utilities.methods.delete_booking(ADMIN_USER, session, booking_id)
    assert delete_booking_response.status_code == 201

    "Then I should't be able to get the booking by ID"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    assert get_booking_response.status_code == 404
