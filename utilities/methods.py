import requests


def create_booking(url, body, header_json):
    requests.post(url=url, json=body, headers=header_json)

def update_booking(url, body, header_json):
    requests.put(url=url, json=body, headers=header_json)


def get_booking_list(url):
    requests.get(url=url)
