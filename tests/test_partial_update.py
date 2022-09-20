from utilities.methods import *
from data.testing_data import *
import pytest

session = create_session()


@pytest.mark.parametrize("booker", bookers)
def test_partial_update_booking(booker):
    """Create booking"""
    results2 = create_booking(booker, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Create authorization token for for access to the PUT and DELETE /booking"
    authorization_url = create_auth_url()
    get_auth(user1, session, authorization_url)

    "Partially update booking "
    url_with_id = create_url_with_id(booking_id)
    patch_booking_response = partial_update_booking(session, url_with_id, json1)
    patch_booking_response_json = patch_booking_response.json()

    assert patch_booking_response_json['firstname'] == "James" and patch_booking_response_json['lastname'] == "Brown"

    "Get list of all bookings"
    list_of_bookings_response = get_list_all_ids(session)
    list_of_bookings_response_json = list_of_bookings_response.json()
    list_of_all_values = [value for elem in list_of_bookings_response_json for value in elem.values()]

    assert list_of_bookings_response.status_code == 200
    assert (booking_id in list_of_all_values)

