from todo import todo

import unittest

class BaseUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = todo
        self.ctx = self.app.app_context()
        self.clt = self.app.test_client()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()


class NewUserSignUpTest(BaseUnitTest):
    def test_signup_link_exists(self):
        resp = self.clt.get('/')
        data = resp.data.decode()
        self.assertIn('<a href="#">Sign Up</a>', data)

    def test_signin_link_exists(self):
        resp = self.clt.get('/')
        data = resp.data.decode()
        self.assertIn('<a href="#">Sign In</a>', data)

