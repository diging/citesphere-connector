import base64
import requests
import os


class CitesphereConnector:
    def __init__(self, api, auth_object):
        self.api = api
        self.auth_object = auth_object
        self.validate()
        self.handle_api_params()

    def validate(self):
        if not hasattr(self.auth_object, "auth_type"):
            raise AttributeError("Missing auth_type attribute")

        if not hasattr(self.auth_object, "headers"):
            raise AttributeError("Missing headers attribute")

        if not hasattr(self.auth_object, "access_token"):
            if not hasattr(self.auth_object, "username") and not hasattr(
                self.auth_object, "password"
            ):
                raise AttributeError(
                    "Either username and password or access_token should be present"
                )

        if (
            not self.auth_object.auth_type == "oauth"
            and not self.auth_object.auth_type == "basic"
        ):
            raise Exception("auth_type should be either oauth or basic")

    def handle_api_params(self):
        if self.auth_object.auth_type == "oauth":
            self.auth_object.headers = {
                "Authorization": f"Bearer {self.auth_object.access_token}",
            }
        elif self.auth_object.auth_type == "basic":
            auth_str = f"{self.auth_object.username}:{self.auth_object.password}"
            auth_b64 = base64.b64encode(auth_str.encode("ascii"))
            self.auth_object.headers = {"Authorization": f"Basic {auth_b64}"}

    def execute_get_request(self, url):
        try:
            response = requests.get(url, headers=self.auth_object.headers)
            return response.json()

        except Exception as exc:
            return {"error_message": str(exc)}

    def execute_post_request(self, url, data, files):
        try:
            requests.post(url, headers=self.auth_object.headers, data=data, files=files)
            # Uncomment for debugging response from Citesphere
            # print(response.status_code)
            # print(response.text)

        except Exception as exc:
            return {"error_message": str(exc)}

    def get_user(self):
        url = f"{self.api}/v1/user"
        return self.execute_get_request(url)

    def check_test(self):
        url = f"{self.api}/v1/test"
        return self.execute_get_request(url)

    def check_access(self, document_id):
        url = f"{self.api}/files/giles/{document_id}/access/check"
        return self.execute_get_request(url)

    # Common method to get data based on endpoint
    def get_data_by_endpoint(self, end_point):
        url = f"{self.api}/v1{end_point}"
        return self.execute_get_request(url)

    def get_groups(self):
        url = f"{self.api}/v1/groups"
        return self.execute_get_request(url)

    def get_group_info(self, group_id):
        url = f"{self.api}/v1/groups/{group_id}"
        return self.execute_get_request(url)

    def get_group_items(self, zotero_group_id, page_number=0):
        url = f"{self.api}/v1/groups/{zotero_group_id}/items"
        if page_number:
            url = f"{url}?&page={page_number}"
        return self.execute_get_request(url)

    def get_collections(self, zotero_group_id):
        url = f"{self.api}/v1/groups/{zotero_group_id}/collections"
        return self.execute_get_request(url)

    def get_collection_items(self, zotero_group_id, collection_id, page_number=0):
        url = (
            f"{self.api}/v1/groups/{zotero_group_id}/collections/{collection_id}/items"
        )
        if page_number:
            url = f"{url}?&page={page_number}"
        return self.execute_get_request(url)

    def get_item_info(self, zotero_group_id, item_id):
        url = f"{self.api}/v1/groups/{zotero_group_id}/items/{item_id}"
        return self.execute_get_request(url)

    def get_collections_by_collection_id(self, zotero_group_id, collection_id):
        url = f"{self.api}/groups/{zotero_group_id}/collections/{collection_id}/collections"
        return self.execute_get_request(url)

    def add_item(self, group_id, data, file_path):
        try:
            with open(file_path, "rb") as file_obj:
                files = [(os.path.basename(file_path), file_obj)]
                request_files = [
                    ("files", (name, file, "application/pdf")) for name, file in files
                ]
                url = f"{self.api}/v1/groups/{group_id}/items/create"

                self.execute_post_request(url, data, request_files)
        except Exception:
            return "Error loading/reading file"
