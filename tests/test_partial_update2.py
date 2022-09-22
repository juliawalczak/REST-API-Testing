import utilities.methods
from data.testing_data import *
import pytest

session = utilities.methods.create_session()


def test_partial_update_booking():
    """Create booking"""
    results2 = utilities.methods.create_booking(booker1, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Create authorization token for for access to the PUT and DELETE /booking"
    authorization_url = utilities.methods.create_auth_url()
    utilities.methods.get_auth(user1, session, authorization_url)

    "Partially update booking "
    url_with_id = utilities.methods.create_url_with_id(booking_id)
    patch_booking_response = utilities.methods.partial_update_booking(session, url_with_id, json2)
    patch_booking_response_json = patch_booking_response.json()

    assert patch_booking_response_json['firstname'] == "Harry" and patch_booking_response_json['lastname'] == "Malfoy" \
           and patch_booking_response_json['totalprice'] == 999 and patch_booking_response_json['depositpaid'] == False \
           and patch_booking_response_json['bookingdates']['checkin'] == '2022-10-01' \
           and patch_booking_response_json['bookingdates']['checkout'] == '2022-10-22' \
           and patch_booking_response_json['additionalneeds'] == 'Dinner'

    "Get created booking by id"
    get_booking_response = utilities.methods.get_item_by_id(url_with_id, session)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert get_booking_response_json['firstname'] == "Harry" and get_booking_response_json['lastname'] == "Malfoy" \
           and get_booking_response_json['totalprice'] == 999 and get_booking_response_json['depositpaid'] == False \
           and get_booking_response_json['bookingdates']['checkin'] == '2022-10-01' \
           and get_booking_response_json['bookingdates']['checkout'] == '2022-10-22' \
           and get_booking_response_json['additionalneeds'] == 'Dinner'
