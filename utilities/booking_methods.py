import requests
from utilities.configuration import *
from data.common_headers import *

BOOKING_PATH = BASE_URL + '/booking'
AUTH_PATH = BASE_URL + '/auth'

def create_session():
    session = requests.Session()
    return session


def booking_path_with_id(booking_id):
    return BASE_URL + '/booking/' + str(booking_id)


def create_booking(booking, session):
    request_body = booking.to_json()
    return session.post(url=BOOKING_PATH, json=request_body, headers=header_json)


def get_all_bookings(session):
    return session.get(BOOKING_PATH)


def get_booking_by_id(booking_id, session):
    url_with_id = booking_path_with_id(booking_id)
    return session.get(url=url_with_id)


def authorize_user(user, session):
    auth_body = user.create_auth_payload()
    response = session.post(url=AUTH_PATH, json=auth_body, headers=header_json)
    user_token = response.json()['token']
    session.headers.update({'Cookie': 'token=' + user_token})


def delete_booking(user, session, booking_id):
    authorize_user(user, session)
    url_with_id = booking_path_with_id(booking_id)
    return session.delete(url=url_with_id)


def partial_update_booking(user, session, booking_id, json):
    authorize_user(user, session)
    url_with_id = booking_path_with_id(booking_id)
    return session.patch(url=url_with_id, json=json)


def update_booking(user, session, booking_id, updated_booking):
    authorize_user(user, session)
    url_with_id = booking_path_with_id(booking_id)
    return session.put(url=url_with_id, json=updated_booking.to_json())
