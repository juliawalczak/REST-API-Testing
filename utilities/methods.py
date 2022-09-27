import requests
from data.testing_data import ADMIN_USER
from utilities.configuration import *
from data.common_headers import *

BOOKING_PATH = BASE_URL + '/booking'
AUTH_PATH = BASE_URL + '/auth'

def create_session():
    session = requests.Session()
    return session


def create_url_with_id(booking_id):
    return BASE_URL + '/booking/' + str(booking_id)


def create_booking(booking, session):
    body = booking.create_booking_payload()
    create_booking_response = session.post(url=BOOKING_PATH, json=body, headers=header_json)
    create_booking_response_json = create_booking_response.json()
    booking_id = create_booking_response_json['bookingid']
    return create_booking_response, create_booking_response_json, booking_id, body


def create_booking_daria(booking, session):
    request_body = booking.create_booking_payload()
    return session.post(url=BOOKING_PATH, json=request_body, headers=header_json)


def get_all_bookings(session):
    return session.get(BOOKING_PATH)


def get_item_by_id(booking_id, session):
    url_with_id = create_url_with_id(booking_id)
    return session.get(url=url_with_id)


def get_auth(user, session):
    auth_body = user.create_auth_payload()
    response = session.post(url=AUTH_PATH, json=auth_body, headers=header_json)
    user_token = response.json()['token']
    session.headers.update({'Cookie': 'token=' + user_token})


def delete_booking(user, session, booking_id):
    get_auth(user, session)
    url_with_id = create_url_with_id(booking_id)
    return session.delete(url=url_with_id)


def partial_update_booking(user, session, booking_id, json):
    get_auth(user, session)
    url_with_id = create_url_with_id(booking_id)
    return session.patch(url=url_with_id, json=json)


def update_booking(user, session, booking_id, updated_booking):
    get_auth(user, session)
    url_with_id = create_url_with_id(booking_id)
    return session.put(url=url_with_id, json=updated_booking.create_booking_payload())
