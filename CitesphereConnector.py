
import urllib2
import json

# CITESPHERE_API = "https://citesphere.instance.org/api/v1"
CITESPHERE_API = "https://diging-dev.asu.edu/citesphere-review/api"


class CitesphereConnector:
    def __init__(self, **kwargs):
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.grant_type = kwargs.get('grant_type')
        self.redirect_uri = kwargs.get('redirect_uri')
        self.authorization_code = kwargs.get('authorization_code')
        self.api_key = None
        self.access_token = kwargs.get('access_token')
        self.validate()

    def validate(self):
        if self.access_token:
            response = self.check_test()
            if response.get("error_message"):
                raise Exception("Access Token is not valid: {}".format(response["error_message"]))
            else:
                return
        if not self.client_id:
            raise Exception("Client Id is required")

        if not self.client_secret:
            raise Exception("Client Secret is required")

        if not self.grant_type:
            raise Exception("Grant Type is required")

        self.get_api_key()


    def get_api_key(self):
        if self.grant_type == "client_credentials":
            url = CITESPHERE_API + "/oauth/token?client_id={}&client_secret={}&grant_type=authorization_code".format(self.client_id, self.client_secret)
            response = urllib2.urlopen(urllib2.Request(url, headers={}))
            data = json.load(response)
        else:
            raise Exception("Invalid Grant Type")

        self.api_key = data["access_token"]

        return None


    def execute_command(self, url):
        try:
            headers = {'Authorization': 'Bearer {}'.format(self.api_key)}
            response = urllib2.urlopen(urllib2.Request(url, headers=headers))
            data = json.load(response)

            return data
        except Exception as exc:
            return {"error_message": str(exc)}


    def get_user(self):
        url = CITESPHERE_API + "/v1/user"
        return self.execute_command(url)


    def check_test(self):
        url = CITESPHERE_API + "/v1/test"
        return self.execute_command(url)


    # Common method to get data based on endpoint
    def get_data_by_endpoint(self, end_point):
        url = CITESPHERE_API + "/v1" + end_point
        return self.execute_command(url)


    def get_groups(self):
        url = CITESPHERE_API + "/v1/groups"
        return self.execute_command(url)


    def get_group_info(self, group_id):
        url = CITESPHERE_API + "/v1/groups/{}".format(group_id)
        return self.execute_command(url)


    def get_group_items(self, zotero_group_id):
        url = CITESPHERE_API + "/v1/groups/{}/items".format(zotero_group_id)
        return self.execute_command(url)


    def get_collections(self, zotero_group_id):
        url = CITESPHERE_API + "/v1/groups/{}/collections".format(zotero_group_id)
        return self.execute_command(url)


    def get_collection_items(self, zotero_group_id, collection_id):
        url = CITESPHERE_API + "/v1/groups/{}/collections/{}/items".format(zotero_group_id, collection_id)
        return self.execute_command(url)


    def get_item_info(self, zotero_group_id, item_id):
        url = CITESPHERE_API + "/v1/groups/{}/items/{}".format(zotero_group_id, item_id)
        return self.execute_command(url)
