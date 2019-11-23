import unittest

from config.test_config import *
from odin.wrapper.proxy import OssCaller
from odin.api.oss import Oss

oss_caller = OssCaller(oss_server_url)
oss = Oss(oss_caller)

class TestOSSMethods(unittest.TestCase):

    def test_get_subscription(self):
        result = oss.get_subscription_token(account_id, subscription_id)
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result) == 2)
        self.assertIn('aps_token', result)
        self.assertIn('controller_uri', result)

    def test_get_services_instances(self):
        result = oss.get_services_instances(application_instance_id)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_get_application_instances(self):
        result = oss.get_application_instances(app_id)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()