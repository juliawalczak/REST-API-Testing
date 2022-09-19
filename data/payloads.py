class BookingData(object):
    """This is a class that describe the booking data."""
    def __init__(self, first_name, last_name, total_price, deposit_paid, check_in, check_out, additional_needs):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.check_in = check_in
        self.check_out = check_out
        self.additional_needs = additional_needs

    def create_booking_payload(self):
        body = {

            "firstname": self.first_name,
            "lastname": self.last_name,
            "totalprice": self.total_price,
            "depositpaid": self.deposit_paid,
            "bookingdates": {
            "checkin": self.check_in,
            "checkout": self.check_out
             },
            "additionalneeds": self.additional_needs
        }
        return body


booker1 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Secret Chamber')
booker2 = BookingData(first_name='Harry', last_name='Potter', total_price=777, deposit_paid=True,
                      check_in='2022-07-07', check_out='2022-07-31', additional_needs='Dobby')