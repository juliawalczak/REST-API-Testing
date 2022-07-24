def create_booking_payload(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds   ):
    body = {

        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    return body
