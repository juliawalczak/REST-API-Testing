import utilities.methods
from data.testing_data import *
import pytest

session = utilities.methods.create_session()


@pytest.mark.parametrize("updated_booker", updated_bookers)
def test_update_booking2(updated_booker):
    """Create booking"""
    results2 = utilities.methods.create_booking(booker1, session)
    create_booking_response = results2[0]
    create_booking_response_json = results2[1]
    booking_id = results2[2]
    body = results2[3]

    assert create_booking_response.status_code == 200
    assert create_booking_response_json['booking'] == body

    "Update booking"
    results3 = utilities.methods.update_booking(ADMIN_USER, session, booking_id, updated_booker)
    update_body = results3[0]
    create_update_response = results3[1]
    create_update_response_json = create_update_response.json()

    assert create_update_response.status_code == 200
    assert update_body == create_update_response_json

    "Get updated booking by id"
    get_booking_response = utilities.methods.get_item_by_id(booking_id, session)
    get_booking_response_json = get_booking_response.json()

    assert get_booking_response.status_code == 200
    assert update_body == get_booking_response_json
