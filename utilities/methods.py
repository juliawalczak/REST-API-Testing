import requests

def create_booking(url, body, header_json):
    requests.post(url, json=body, headers=header_json, )
