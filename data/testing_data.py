from data.user import *
from data.payloads import *

user1 = UserData(username='admin', password='password123')
booker1 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Secret Chamber')
booker2 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Dobby')
booker3 = BookingData(first_name='George', last_name='Weasley', total_price=1902, deposit_paid=False,
                      check_in='2022-07-02', check_out='2022-08-31', additional_needs='Breakfast')
booker4 = BookingData(first_name='Lily', last_name='Snape', total_price=299, deposit_paid=True,
                      check_in='2022-05-07', check_out='2022-05-17', additional_needs='None')


bookers = [booker1, booker2]
updated_bookers = [booker3, booker4]
json1 = {
    "firstname": "James",
    "lastname": "Brown"
}

json2 = {
    "firstname": "Lily",
    "lastname": "Xyz"
}
