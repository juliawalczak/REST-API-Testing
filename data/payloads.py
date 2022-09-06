class BookingData(object):
    "This is a class that describe the booking data."
    def __int__(self, first_name, last_name, total_price, deposit_paid, check_in, check_out, additional_needs):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.check_in = check_in
        self.check_out = check_out
        self.additional_needs = additional_needs

    def create_booking_payload(self):
        body = {

            "firstname": first_name,
            "lastname": last_name,
            "totalprice": total_price,
            "depositpaid": deposit_paid,
            "bookingdates": {
            "checkin": check_in,
            "checkout": check_out
             },
            "additionalneeds": additional_needs
        }
        return body
