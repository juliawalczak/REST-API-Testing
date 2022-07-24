import requests
from utilities.configuration import *
from payloads import *

url = get_config()['API']['main_endpoint']
headers = {"Content-Type": "application/json"}
create_booking_response = requests.post(url, json=create_booking_payload(
    "Harry", "Potter", 777, "true", "2022-07-07", "2022-07-31", "Secret Chamber"), headers=headers, )

response_json = create_booking_response.json()

assert create_booking_response.status_code == 200
expected_booking_details = {'firstname': 'Harry', 'lastname': 'Potter', 'totalprice': 777, 'depositpaid': True, 'bookingdates': {'checkin': '2022-07-07', 'checkout': '2022-07-31'}, 'additionalneeds': 'Secret Chamber'}
assert expected_booking_details == response_json['booking']


