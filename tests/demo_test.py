import requests
from utilities.configuration import *
from data.payloads import *
from data.payload_data import *
from data.common_headers import *
from utilities.methods import *

url = get_config()['API']['main_endpoint'] + '/booking'
body = create_booking(BookingData.first_name, BookingData.last_name, BookingData.total_price, BookingData.deposit_paid, BookingData.check_in, BookingData.check_out, BookingData.additional_needs)
create_booking_response = requests.post(url, json=body, headers=header_json, )

response_json = create_booking_response.json()


assert create_booking_response.status_code == 200
assert body == response_json['booking']


