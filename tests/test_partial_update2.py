import utilities.methods
from data.testing_data import *

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

    "Partially update booking "
    patch_booking_response = utilities.methods.partial_update_booking(ADMIN_USER, session, booking_id, json2)
    patch_booking_response_json = patch_booking_response.json()

    assert patch_booking_response_json['firstname'] == booker1.first_name
    assert patch_booking_response_json['lastname'] == json2['lastname']
    assert patch_booking_response_json['totalprice'] == 999
    assert patch_booking_response_json['depositpaid'] == False
    assert patch_booking_response_json['bookingdates']['checkin'] == '2022-10-01'
    assert patch_booking_response_json['bookingdates']['checkout'] == '2022-10-22'
    assert patch_booking_response_json['additionalneeds'] == 'Dinner'

    "Get created booking by id"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert get_booking_response_json['firstname'] == "Harry"
    assert get_booking_response_json['lastname'] == "Malfoy"
    assert get_booking_response_json['totalprice'] == 999
    assert get_booking_response_json['depositpaid'] == False
    assert get_booking_response_json['bookingdates']['checkin'] == '2022-10-01'
    assert get_booking_response_json['bookingdates']['checkout'] == '2022-10-22'
    assert get_booking_response_json['additionalneeds'] == 'Dinner'
