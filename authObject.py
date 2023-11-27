class AuthObject:
    def __init__(self, authType=None, headers=None, username=None, password=None, access_token=None):
        self.authType = authType
        self.headers = headers
        self.username = username
        self.password = password
        self.access_token = access_token