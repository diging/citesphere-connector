import unittest
from unittest.mock import Mock, patch, MagicMock
from CitesphereConnector import CitesphereConnector
from authObject import AuthObject
from http import HTTPStatus

class EmptyObject:
    pass


class CitesphereConnectorTest(unittest.TestCase):
    def test_validate_method(self):
        auth_object = AuthObject()
        with self.assertRaises(Exception):
            CitesphereConnector("example.com", auth_object)
        pass

    def test_validate_method_attribute_error(self):
        auth_object = EmptyObject()
        with self.assertRaises(AttributeError):
            CitesphereConnector("example.com", auth_object)
        pass

    @patch('CitesphereConnector.CitesphereConnector.get_groups')
    def test_api_called(self, mock_get_groups):
        auth_object = AuthObject()
        auth_object.authType = 'oauth'
        mock_get_groups.return_value = Mock()
        mock_get_groups.return_value.json.return_value = [{'name': "vogon", 'id': 1}]
        connector = CitesphereConnector("example.com", auth_object)
        print(connector.get_groups())
        self.assertEqual(connector.get_groups()[0]['id'], 1)
        pass


if __name__ == '__main__':
    unittest.main()