from utilities.configuration import *
from data.payloads import *
from data.common_headers import *
from utilities.methods import *

url = get_config()['API']['main_endpoint'] + '/booking'
body = BookingData.create_booking_payload(booker1)

create_booking_response = requests.post(url, json=body, headers=header_json, )

response_json = create_booking_response.json()

assert create_booking_response.status_code == 200
assert body == response_json['booking']


