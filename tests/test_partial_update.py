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
    patch_booking_response = utilities.methods.partial_update_booking(ADMIN_USER, session, booking_id, json1)
    patch_booking_response_json = patch_booking_response.json()

    assert patch_booking_response_json['firstname'] == "James"
    assert patch_booking_response_json['lastname'] == "Brown"
    assert patch_booking_response_json['totalprice'] == 777
    assert patch_booking_response_json['depositpaid'] ==True
    assert patch_booking_response_json['bookingdates']['checkin'] == '2022-07-07'
    assert patch_booking_response_json['bookingdates']['checkout'] == '2022-07-31'
    assert patch_booking_response_json['additionalneeds'] == 'Secret Chamber'

    "Get list of all bookings"
    list_of_bookings_response = utilities.methods.get_all_bookings(session)
    list_of_bookings_response_json = list_of_bookings_response.json()
    list_of_all_values = [value for elem in list_of_bookings_response_json for value in elem.values()]

    assert list_of_bookings_response.status_code == 200
    assert (booking_id in list_of_all_values)
