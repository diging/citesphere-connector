class AuthObject:
    def __init__(
        self,
        auth_type=None,
        access_token=None,
        headers=None,
        username=None,
        password=None,
    ):
        self.auth_type = auth_type
        self.access_token = access_token
        self.headers = headers
        self.username = username
        self.password = password
