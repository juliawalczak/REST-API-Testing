import utilities.methods
from data.testing_data import *
import pytest

session = utilities.methods.create_session()


@pytest.mark.parametrize("booker", bookers)
def test_create_booking2(booker):
    """Create booking"""
    results2 = utilities.methods.create_booking(booker, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Get created booking by id"
    url_with_id = utilities.methods.create_url_with_id(booking_id)
    get_booking_response = utilities.methods.get_item_by_id(url_with_id, session)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert body == get_booking_response_json
