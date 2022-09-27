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

def booking_data_from_json(json):
    return BookingData(
        first_name=json["firstname"],
        last_name=json["lastname"],
        total_price=json["totalprice"],
        deposit_paid=json["depositpaid"],
        check_in=json["bookingdates.checkin"],
        check_out=json["bookingdates.checkout"],
        additional_needs=json["additionalneeds"]
    )