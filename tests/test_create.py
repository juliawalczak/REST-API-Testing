from utilities.methods import *
from utilities.methods import *
from data.testing_data import *
import pytest

session = create_session()


@pytest.mark.parametrize("booker", bookers)
def test_create_booking(booker):
    """Create booking"""
    results2 = create_booking(booker, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Get list of all bookings"
    results2 = get_list_all_ids(session)
    list_of_bookings_response = results2[0]
    list_of_bookings_response_json = results2[1]

    assert list_of_bookings_response.status_code == 200
    assert (booking['bookingid'] == booking_id for booking in list_of_bookings_response_json)
