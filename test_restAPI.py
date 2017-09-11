import unittest
import re
from restAPI_actions import ControlRestAPI

REGEX_EMAIL = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
REGEX_ID = re.compile(r"(?<![-.])\b[0-9]+\b(?!\.[0-9])")
REGEX_TEXT = re.compile(r".*\S.*")


class TestRestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rest = ControlRestAPI()
        cls.data = cls.rest.get_user_data()
        cls.email_address = cls.data['email']

    def test_email_address(self):
        self.result_email = REGEX_EMAIL.match(self.email_address)
        self.assertTrue(bool(self.result_email))

    def test_validate_id(self):
        for post_id in self.rest.get_users_specific_data('id'):
            self.result_id = REGEX_ID.match(str(post_id))
            self.assertTrue(bool(self.result_id))

    def test_validate_title(self):
        for title in self.rest.get_users_specific_data('title'):
            self.result_title = REGEX_TEXT.match(title)
            self.assertTrue(bool(self.result_title))

    def test_validate_body(self):
        for body in self.rest.get_users_specific_data('body'):
            self.result_body = REGEX_TEXT.match(body)
            self.assertTrue(bool(self.result_body))

    def test_post_successful(self):
        self.return_code = self.rest.post_new_data()
        self.assertEqual(str(self.return_code), '201')

    @classmethod
    def tearDownClass(cls):
        cls.rest = None
