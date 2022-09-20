from data.user import *
from data.payloads import *

user1 = UserData(username='admin', password='password123')
booker1 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Secret Chamber')
booker2 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Dobby')

bookers = [booker1, booker2]

json1 = {
    "firstname": "James",
    "lastname": "Brown"
}

json2 = {
    "firstname": "Lily",
    "lastname": "Xyz"
}
