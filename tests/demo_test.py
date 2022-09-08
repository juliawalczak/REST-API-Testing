import requests

from utilities.configuration import *
from data.payloads import *
from data.user import *
from data.common_headers import *
from utilities.methods import *

s = requests.Session()

"Create booking"
url = get_config()['API']['main_endpoint'] + '/booking'
body = booker1.create_booking_payload()
create_booking_response = s.post(url, json=body, headers=header_json, )

response_json = create_booking_response.json()

assert create_booking_response.status_code == 200
assert body == response_json['booking']

booking_id = response_json['bookingid']

"Get list of all bookings"
create_booking_response2 = s.get(url)
response_json2 = create_booking_response2.json()

"Create authorization token for for access to the PUT and DELETE /booking"
authorization_url = get_config()['API']['main_endpoint'] + '/auth'
auth_body = user1.create_auth_payload()
create_token_response = s.post(url=authorization_url, json=auth_body, headers=header_json, )
response_json3 = create_token_response.json()
user_token = 'token=' + response_json3['token']
s.headers.update({'Cookie': user_token})

"Update booking"
url4 = get_config()['API']['main_endpoint'] + '/booking/' + str(booking_id)
body4 = booker2.create_booking_payload()
create_update_response = s.put(url=url4, json=body4)
response_json4 = create_update_response.json()

assert create_update_response.status_code == 200
assert body4 == response_json4


