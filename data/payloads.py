def create_booking_payload(first_name, last_name, total_price, deposit_paid,
                           check_in, check_out, additional_needs):
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
