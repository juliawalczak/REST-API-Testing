from utilities.methods import *
from data.testing_data import *
import pytest

session = create_session()


@pytest.mark.parametrize("updated_booker", updated_bookers)
def test_update_booking(updated_booker):
    """Create booking"""
    results2 = create_booking(booker1, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Create authorization token for for access to the PUT and DELETE /booking"
    authorization_url = create_auth_url()
    get_auth(user1, session, authorization_url)

    "Update booking"
    url_with_id = create_url_with_id(booking_id)
    results3 = update_booking(session, url_with_id, updated_booker)
    update_body = results3[0]
    create_update_response = results3[1]
    create_update_response_json = create_update_response.json()

    assert create_update_response.status_code == 200
    assert update_body == create_update_response_json

    "Get list of all bookings"
    list_of_bookings_response_json = get_list_all_ids(session)[1]
    assert (booking['bookingid'] == booking_id for booking in list_of_bookings_response_json)
