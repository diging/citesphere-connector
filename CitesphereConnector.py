
import urllib.request as urllib2
import json


class BearerAccessTokenAuthorization:
    def __init__(self, access_token):
        self.headers = {'Authorization': 'Bearer {}'.format(access_token)}


class OAuth2ClientAuthorization:
    def __init__(self, api, kwargs):
        self.api = api
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.headers = BearerAccessTokenAuthorization(self.get_access_token()).headers

    def get_access_token(self):
        url = self.api + "/oauth/token?client_id={}&client_secret={}&grant_type=client_credentials".format(
            self.client_id, self.client_secret)
        response = urllib2.urlopen(urllib2.Request(url, headers={}))
        data = json.load(response)

        return data['access_token']


def validate(kwargs, api):
    if not api:
        raise Exception("API is required")

    if not kwargs.get('access_token') and not (kwargs.get('grant_type') and kwargs.get('client_id') and kwargs.get('client_secret')):
        raise Exception("Insufficient authentication details. Either Access token is required or client id, secret, grant type are required")


class CitesphereConnector:
    def __init__(self, api, **kwargs):
        self.api = api
        validate(kwargs, api)
        self.oauth_object = self.get_oauth_object(kwargs)

    def get_oauth_object(self, kwargs):
        if kwargs.get('grant_type') == "client_credentials":
            return OAuth2ClientAuthorization(self.api, kwargs)
        else:
            return BearerAccessTokenAuthorization(kwargs.get('access_token'))

    def execute_command(self, url):
        try:
            response = urllib2.urlopen(urllib2.Request(url, headers=self.oauth_object.headers))
            data = json.load(response)

            return data
        except Exception as exc:
            return {"error_message": str(exc)}

    def get_user(self):
        url = self.api + "/v1/user"
        return self.execute_command(url)

    def check_test(self):
        url = self.api + "/v1/test"
        return self.execute_command(url)

    # Common method to get data based on endpoint
    def get_data_by_endpoint(self, end_point):
        url = self.api + "/v1" + end_point
        return self.execute_command(url)

    def get_groups(self):
        url = self.api + "/v1/groups"
        return self.execute_command(url)

    def get_group_info(self, group_id):
        url = self.api + "/v1/groups/{}".format(group_id)
        return self.execute_command(url)

    def get_group_items(self, zotero_group_id):
        url = self.api + "/v1/groups/{}/items".format(zotero_group_id)
        return self.execute_command(url)

    def get_collections(self, zotero_group_id):
        url = self.api + "/v1/groups/{}/collections".format(zotero_group_id)
        return self.execute_command(url)

    def get_collection_items(self, zotero_group_id, collection_id):
        url = self.api + "/v1/groups/{}/collections/{}/items".format(zotero_group_id, collection_id)
        return self.execute_command(url)

    def get_item_info(self, zotero_group_id, item_id):
        url = self.api + "/v1/groups/{}/items/{}".format(zotero_group_id, item_id)
        return self.execute_command(url)
