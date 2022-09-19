from utilities.configuration import *
from data.payloads import *
from data.common_headers import *
from utilities.methods import *
from data.user import *
import pytest


def test_delete_booking2():
    session = requests.Session()

    "Create booking"

    url = main_endpoint + '/booking'
    body = booker1.create_booking_payload()
    create_booking_response = session.post(url, json=body, headers=header_json, )
    create_booking_response_json = create_booking_response.json()

    booking_id = create_booking_response_json['bookingid']

    assert create_booking_response.status_code == 200
    assert body == create_booking_response_json['booking']

    "Create authorization token for for access to the PUT and DELETE /booking"
    authorization_url = main_endpoint + '/auth'
    auth_body = user1.create_auth_payload()
    create_token_response = session.post(url=authorization_url, json=auth_body, headers=header_json)
    create_token_response_json = create_token_response.json()

    user_token = 'token=' + create_token_response_json['token']
    session.headers.update({'Cookie': user_token})

    "Delete booking"
    url_with_id = main_endpoint + '/booking/' + str(booking_id)
    delete_booking_response = session.delete(url=url_with_id)
    assert delete_booking_response.status_code == 201

    "Get  booking by id"
    get_booking_response = session.get(url=url_with_id)
    assert get_booking_response.status_code == 404


