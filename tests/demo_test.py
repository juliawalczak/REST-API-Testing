from utilities.configuration import *
from data.payloads import *
from data.user import *
from data.common_headers import *
from utilities.methods import *

"Create booking"
url = get_config()['API']['main_endpoint'] + '/booking'
body = booker1.create_booking_payload()
create_booking_response = requests.post(url, json=body, headers=header_json, )

response_json = create_booking_response.json()

assert create_booking_response.status_code == 200
assert body == response_json['booking']

booking_id = response_json['bookingid']

"Get list of all bookings"
create_booking_response2 = requests.get(url)
response_json2 = create_booking_response2.json()
print(response_json2)

"Create authorization token for for access to the PUT and DELETE /booking"
authorization_url = get_config()['API']['main_endpoint'] + '/auth'
auth_body = user1.create_auth_payload()
create_token_response = requests.post(url=authorization_url, json=auth_body, headers=header_json, )
response_json3 = create_token_response.json()
user_token = response_json3['token']

"Update booking"
url4 = get_config()['API']['main_endpoint'] + '/' + str(booking_id)
body4 = booker2.create_booking_payload()
create_update_response = requests.put(url=url4, json=body4, headers={"Cookie": user_token}, )
response_json4 = create_update_response.json()
print(response_json4)

