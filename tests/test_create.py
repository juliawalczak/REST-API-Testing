from utilities.configuration import *
from data.payloads import *
from data.common_headers import *
from utilities.methods import *


def test_create_booking():
    session = requests.Session()

    "Create booking"

    url = main_endpoint + '/booking'
    body = booker1.create_booking_payload()
    create_booking_response = session.post(url, json=body, headers=header_json, )
    create_booking_response_json = create_booking_response.json()

    booking_id = create_booking_response_json['bookingid']

    assert create_booking_response.status_code == 200
    assert body == create_booking_response_json['booking']

    "Get list of all bookings"
    list_of_bookings_response = session.get(url)
    list_of_bookings_response_json = list_of_bookings_response.json()

    assert list_of_bookings_response.status_code == 200
    assert (booking['bookingid'] == booking_id for booking in list_of_bookings_response_json)
