
import urllib2
import json

CITESPHERE_API = "https://citesphere.instance.org/api/v1"


class CitesphereConnector:
    def __init__(self, client_id, client_secret, end_point=None):
        self.api_key = self.get_api_key(client_id, client_secret)
        self.end_point = end_point

    def get_api_key(self, client_id, client_secret):
        url = CITESPHERE_API + "/oauth/token?client_id={}&client_secret={}&grant_type=authorization_code".format(client_id, client_secret)
        response = urllib2.urlopen(urllib2.Request(url, headers={}))
        data = json.load(response)

        return data["access_token"]

    def execute_command(self, url):
        try:
            headers = {'Authorization': 'Bearer {}'.format(self.api_key)}
            response = urllib2.urlopen(urllib2.Request(url, headers=headers))
            data = json.load(response)

            return data
        except Exception as exc:
            return {"error_message": str(exc)}

    def get_user(self):
        url = CITESPHERE_API + "/user"
        return self.execute_command(url)

    def check_test(self):
        url = CITESPHERE_API + "/test"
        return self.execute_command(url)

    # Common method to get data for all endpoints
    def get_data(self, end_point):
        url = CITESPHERE_API + end_point
        return self.execute_command(url)
