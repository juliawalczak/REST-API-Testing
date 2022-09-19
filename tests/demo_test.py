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
create_booking_response_json = create_booking_response.json()

booking_id = create_booking_response_json['bookingid']

assert create_booking_response.status_code == 200
assert body == create_booking_response_json['booking']

"Get list of all bookings"
list_of_bookings_response = s.get(url)
list_of_bookings_response_json = list_of_bookings_response.json()

assert list_of_bookings_response.status_code == 200
assert (d['bookingid'] == booking_id for d in list_of_bookings_response_json)

"Create authorization token for for access to the PUT and DELETE /booking"
authorization_url = get_config()['API']['main_endpoint'] + '/auth'
auth_body = user1.create_auth_payload()
create_token_response = s.post(url=authorization_url, json=auth_body, headers=header_json, )
create_token_response_json = create_token_response.json()

user_token = 'token=' + create_token_response_json['token']
s.headers.update({'Cookie': user_token})

"Update booking"
url_with_id = get_config()['API']['main_endpoint'] + '/booking/' + str(booking_id)
update_body = booker2.create_booking_payload()
create_update_response = s.put(url=url_with_id, json=update_body)
create_update_response_json = create_update_response.json()

assert create_update_response.status_code == 200
assert update_body == create_update_response_json

"Get updated booking by id"
get_booking_response = s.get(url=url_with_id)
get_booking_response_json = get_booking_response.json()

assert get_booking_response.status_code == 200
assert update_body == get_booking_response_json

"Partially update booking "
patch_booking_response = s.patch(url=url_with_id, json={
    "firstname": "James",
    "lastname": "Brown"
})

patch_booking_response_json = patch_booking_response.json()
assert patch_booking_response_json['firstname'] == "James" and patch_booking_response_json['lastname'] == "Brown"

"Delete booking"
delete_booking_response = s.delete(url=url_with_id)
assert delete_booking_response.status_code == 201
