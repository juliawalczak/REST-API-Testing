from data.user import *
from data.payloads import *

ADMIN_USER = UserData(username='admin', password='password123')

BOOKING_1 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Secret Chamber')

BOOKING_2 = BookingData(first_name='George', last_name='Weasley', total_price=1902, deposit_paid=False,
                      check_in='2022-07-02', check_out='2022-08-31', additional_needs='Breakfast')


UPDATED_BOOKING_JSON = {
    "lastname": 'Malfoy',
    "totalprice": 999,
    "depositpaid": False,
    "bookingdates": {
        "checkin": '2022-10-01',
        "checkout": '2022-10-22',
    },
    "additionalneeds": 'Dinner'
}
