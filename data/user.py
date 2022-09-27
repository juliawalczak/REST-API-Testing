class UserData(object):
    """This is a class that describe the user data."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_auth_payload(self):
        return {
            "username": self.username,
            "password": self.password,
        }
