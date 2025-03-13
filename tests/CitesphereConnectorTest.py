import unittest
from unittest.mock import patch, mock_open
from src.CitesphereConnector import CitesphereConnector
from src.AuthObject import AuthObject


class EmptyObject:
    pass


class CitesphereConnectorTest(unittest.TestCase):
    def setUp(self):
        self.auth_object = AuthObject()
        self.auth_object.authType = "oauth"

    def tearDown(self):
        del self.auth_object

    def test_validate_method(self):
        self.auth_object = AuthObject()
        with self.assertRaises(Exception):
            CitesphereConnector("example.com", self.auth_object)
        pass

    def test_validate_method_attribute_error(self):
        self.auth_object = EmptyObject()
        with self.assertRaises(AttributeError):
            CitesphereConnector("example.com", self.auth_object)
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_groups")
    def test_get_groups(self, mock_get_groups):
        mock_get_groups.return_value = [{"name": "vogon", "id": 1}]
        c = CitesphereConnector("test_get_groups.com", self.auth_object)
        result = c.get_groups()
        c.get_groups.assert_called_once()
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "vogon")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.check_access")
    def test_check_access(self, mock_check_access):
        mock_check_access.return_value = "200 OK"
        c = CitesphereConnector("test_check_access.com", self.auth_object)
        result = c.check_access("example_doc_id")
        c.check_access.assert_called_once()
        self.assertEqual(result, "200 OK")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_user")
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = {
            "username": "test",
            "email": "test@test.com",
            "firstName": "get",
            "lastName": "user",
        }
        c = CitesphereConnector("test_get_user.com", self.auth_object)
        result = c.get_user()
        c.get_user.assert_called_once()
        self.assertEqual(result["username"], "test")
        self.assertEqual(result["email"], "test@test.com")
        self.assertEqual(result["firstName"], "get")
        self.assertEqual(result["lastName"], "user")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_group_info")
    def test_get_group_info(self, mock_get_group_info):
        mock_get_group_info.return_value = {"id": 1, "name": "test_get_group_info"}
        c = CitesphereConnector("test_get_group_info.com", self.auth_object)
        result = c.get_group_info(1)
        c.get_group_info.assert_called_once()
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "test_get_group_info")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_group_items")
    def test_get_group_items(self, mock_get_group_items):
        mock_get_group_items.return_value = {
            "group": {"id": 1, "name": "test_get_group_items_group"},
            "items": [
                {"key": "TEST", "group": 1, "title": "test_get_group_items_item"}
            ],
        }
        c = CitesphereConnector("test_get_group_items.com", self.auth_object)
        result = c.get_group_items(1)
        c.get_group_items.assert_called_once()
        self.assertEqual(result["group"]["id"], 1)
        self.assertEqual(result["group"]["name"], "test_get_group_items_group")
        self.assertEqual(result["items"][0]["key"], "TEST")
        self.assertEqual(result["items"][0]["group"], 1)
        self.assertEqual(result["items"][0]["title"], "test_get_group_items_item")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_collections")
    def test_get_collections(self, mock_get_collections):
        mock_get_collections.return_value = {
            "group": {"id": 1, "name": "test_get_collections_group"},
            "collections": [
                {
                    "id": {"timestamp": 1, "date": 1},
                    "key": "TEST",
                    "groupId": 1,
                    "name": "test_get_collections_collection",
                }
            ],
        }
        c = CitesphereConnector("test_get_collections.com", self.auth_object)
        result = c.get_collections(1)
        c.get_collections.assert_called_once()
        self.assertEqual(result["group"]["id"], 1)
        self.assertEqual(result["group"]["name"], "test_get_collections_group")
        self.assertEqual(result["collections"][0]["id"]["timestamp"], 1)
        self.assertEqual(result["collections"][0]["key"], "TEST")
        self.assertEqual(result["collections"][0]["groupId"], 1)
        self.assertEqual(
            result["collections"][0]["name"], "test_get_collections_collection"
        )
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_collection_items")
    def test_get_collection_items(self, mock_get_collection_items):
        mock_get_collection_items.return_value = {
            "group": {"id": 1, "name": "test_get_collection_items_group"},
            "items": [
                {"key": "TEST", "group": 1, "title": "test_get_collection_items_item"}
            ],
        }
        c = CitesphereConnector("test_get_collection_items.com", self.auth_object)
        result = c.get_collection_items(1, 1)
        c.get_collection_items.assert_called_once()
        self.assertEqual(result["group"]["id"], 1)
        self.assertEqual(result["group"]["name"], "test_get_collection_items_group")
        self.assertEqual(result["items"][0]["key"], "TEST")
        self.assertEqual(result["items"][0]["group"], 1)
        self.assertEqual(result["items"][0]["title"], "test_get_collection_items_item")
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.get_item_info")
    def test_get_item_info(self, mock_get_item_info):
        mock_get_item_info.return_value = {
            "item": {"key": "TEST", "group": "1", "title": "test_get_item_info_item"},
        }
        c = CitesphereConnector("test_get_item_info.com", self.auth_object)
        result = c.get_item_info(1, 1)
        c.get_item_info.assert_called_once()
        self.assertEqual(result["item"]["key"], "TEST")
        self.assertEqual(result["item"]["group"], "1")
        self.assertEqual(result["item"]["title"], "test_get_item_info_item")
        pass

    @patch(
        "src.CitesphereConnector.CitesphereConnector.get_collections_by_collection_id"
    )
    def test_get_collections_by_collection_id(
        self, mock_get_collections_by_collection_id
    ):
        mock_get_collections_by_collection_id.return_value = {
            "group": {"id": 1, "name": "test_get_collections_by_collection_id_group"},
            "items": [
                {
                    "key": "TEST",
                    "group": 1,
                    "title": "test_get_collections_by_collection_id_item",
                }
            ],
        }
        c = CitesphereConnector(
            "test_get_collections_by_collection_id.com", self.auth_object
        )
        result = c.get_collections_by_collection_id(1, 1)
        c.get_collections_by_collection_id.assert_called_once()
        self.assertEqual(result["group"]["id"], 1)
        self.assertEqual(
            result["group"]["name"], "test_get_collections_by_collection_id_group"
        )
        self.assertEqual(result["items"][0]["key"], "TEST")
        self.assertEqual(result["items"][0]["group"], 1)
        self.assertEqual(
            result["items"][0]["title"], "test_get_collections_by_collection_id_item"
        )
        pass

    @patch("src.CitesphereConnector.CitesphereConnector.add_item")
    def test_add_item(self, mock_add_item):
        mock_add_item.return_value = {
            "key": "TEST",
            "group": "1",
            "title": "test_add_item",
        }
        c = CitesphereConnector("test_add_item.com", self.auth_object)
        result = c.add_item(1, {"data": "test"}, "path/to/file")
        c.add_item.assert_called_once()
        self.assertEqual(result["key"], "TEST")
        self.assertEqual(result["group"], "1")
        self.assertEqual(result["title"], "test_add_item")
        pass

    @patch("builtins.open", new_callable=mock_open)
    def test_add_item_exception(self, mock_open):
        mock_open.side_effect = Exception()
        c = CitesphereConnector("test_add_item_exception.com", self.auth_object)
        result = c.add_item(1, {"data": "test"}, "path/to/file")
        mock_open.assert_called_once_with("path/to/file", "rb")
        self.assertEqual(result, "Error loading/reading file")
        pass


if __name__ == "__main__":
    unittest.main()
