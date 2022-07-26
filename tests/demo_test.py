import requests
from utilities.configuration import *
from data.payloads import *
from data.payload_data import *

url = get_config()['API']['main_endpoint']
headers = {"Content-Type": "application/json"}
create_booking_response = requests.post(url, json=create_booking_payload(
    first_name, last_name, total_price, deposit_paid, check_in, check_out, additional_needs), headers=headers, )

response_json = create_booking_response.json()

assert create_booking_response.status_code == 200
expected_booking_details = {'firstname': 'Harry', 'lastname': 'Potter', 'totalprice': 777,
                            'depositpaid': True, 'bookingdates': {'checkin': '2022-07-07',
                                                                  'checkout': '2022-07-31'},
                            'additionalneeds': 'Secret Chamber'}
assert expected_booking_details == response_json['booking']

print(response_json)
