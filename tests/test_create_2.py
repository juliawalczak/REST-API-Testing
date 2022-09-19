from utilities.configuration import *
from data.payloads import *
from data.common_headers import *
from utilities.methods import *


def test_create_booking2():
    session = requests.Session()

    "Create booking"

    url = main_endpoint + '/booking'
    body = booker1.create_booking_payload()
    create_booking_response = session.post(url, json=body, headers=header_json, )
    create_booking_response_json = create_booking_response.json()

    booking_id = create_booking_response_json['bookingid']

    assert create_booking_response.status_code == 200
    assert body == create_booking_response_json['booking']

    "Get created booking by id"
    url_with_id = main_endpoint + '/booking/' + str(booking_id)
    get_booking_response = session.get(url=url_with_id)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert body == get_booking_response_json
