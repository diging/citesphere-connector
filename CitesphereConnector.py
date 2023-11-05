import urllib.request as urllib2
import json
import base64


class CitesphereConnector:
    def __init__(self, api, auth_token_object):
        self.api = api
        self.auth_token_object = auth_token_object
        self.validate()
        self.handle_api_params()

    def validate(self):
        if not hasattr(self.auth_token_object, 'authType'):
            raise AttributeError('Missing authType attribute')

        if not hasattr(self.auth_token_object, 'headers'):
            raise AttributeError('Missing headers attribute')

        if not hasattr(self.auth_token_object, 'access_token'):
            if not hasattr(self.auth_token_object, 'username') and not hasattr(self.auth_token_object, 'password'):
                raise AttributeError('Either username and password or access_token should be present')

        if not self.auth_token_object.authType == 'oauth' and not self.auth_token_object.authType == 'basic':
            raise Exception("authType should be either oauth or basic")

    def handle_api_params(self):
        if self.auth_token_object.authType == "oauth":
            self.auth_token_object.headers = {'Authorization': 'Bearer {}'.format(self.auth_token_object.access_token)}
        elif self.auth_token_object.authType == "basic":
            auth_str = '{}:{}'.format(self.auth_token_object.username, self.auth_token_object.password)
            auth_b64 = base64.b64encode(auth_str.encode('ascii'))
            self.auth_token_object.headers = {'Authorization': 'Basic {}'.format(auth_b64)}

    def execute_command(self, url):
        try:
            response = urllib2.urlopen(urllib2.Request(url, headers=self.auth_token_object.headers))
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
    
    def get_collection_items_pg(self, zotero_group_id, collection_id,pg_number):
        url = self.api + "/v1/groups/{}/collections/{}/items?&page={}".format(zotero_group_id, collection_id,pg_number)
        return self.execute_command(url)

    def get_collection_items(self, zotero_group_id, collection_id):
        url = self.api + "/v1/groups/{}/collections/{}/items".format(zotero_group_id, collection_id)
        return self.execute_command(url)

    def get_item_info(self, zotero_group_id, item_id):
        url = self.api + "/v1/groups/{}/items/{}".format(zotero_group_id, item_id)
        return self.execute_command(url)
    
    def get_collection_items_pg(self, zotero_group_id, collection_id,pagenumber):
        url = self.api + "/v1/groups/{}/collections/{}/items?&page={}".format(zotero_group_id, collection_id,pagenumber)
        return self.execute_command(url)
