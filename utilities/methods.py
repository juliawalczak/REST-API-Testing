import requests
from utilities.configuration import *
from data.common_headers import *

url = main_endpoint + '/booking'

def create_session():
    session = requests.Session()
    return session


def create_url_with_id(booking_id):
    url_with_id = main_endpoint + '/booking/' + str(booking_id)
    return url_with_id


def create_auth_url():
    authorization_url = main_endpoint + '/auth'
    return authorization_url

def create_booking(booker, session):
    body = booker.create_booking_payload()
    create_booking_response = session.post(url=url, json=body, headers=header_json)
    create_booking_response_json = create_booking_response.json()
    booking_id = create_booking_response_json['bookingid']
    return create_booking_response, create_booking_response_json, booking_id, body


def get_list_all_ids(session):
    list_of_bookings_response = session.get(url)
    list_of_bookings_response_json = list_of_bookings_response.json()
    return list_of_bookings_response, list_of_bookings_response_json


def get_item_by_id(url_with_id, session):
    get_booking_response = session.get(url=url_with_id)
    return get_booking_response

def get_auth(user, session, authorization_url):
    auth_body = user.create_auth_payload()
    create_token_response = session.post(url=authorization_url, json=auth_body, headers=header_json)
    create_token_response_json = create_token_response.json()
    user_token = 'token=' + create_token_response_json['token']
    session.headers.update({'Cookie': user_token})

def delete_booking(session, url_with_id):
    delete_booking_response = session.delete(url=url_with_id)
    return delete_booking_response

def partial_update(session, url_with_id, json):
    patch_booking_response = session.patch(url=url_with_id, json=json)
    return patch_booking_response

def update_booking(session, url_with_id, updated_booker):
    update_body = updated_booker.create_booking_payload()
    create_update_response = session.put(url=url_with_id, json=update_body)
    return update_body, create_update_response
