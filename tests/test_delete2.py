import utilities.methods
from data.testing_data import *
import pytest

session = utilities.methods.create_session()


@pytest.mark.parametrize("booker", bookers)
def test_delete_booking2(booker):
    """Create booking"""
    results2 = utilities.methods.create_booking(booker, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Create authorization token for for access to the PUT and DELETE /booking"
    authorization_url = utilities.methods.create_auth_url()
    utilities.methods.get_auth(user1, session, authorization_url)

    "Delete booking"
    url_with_id = utilities.methods.create_url_with_id(booking_id)
    delete_booking_response = utilities.methods.delete_booking(session, url_with_id)
    assert delete_booking_response.status_code == 201

    "Get  booking by id"
    get_booking_response = utilities.methods.get_item_by_id(url_with_id, session)
    assert get_booking_response.status_code == 404
