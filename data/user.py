class UserData(object):
    """This is a class that describe the user data."""
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def create_auth_payload(self):
        auth_body = {

            "username": self.username,
            "password": self.password,

             }
        return auth_body


user1 = UserData(username='admin', password='password123')