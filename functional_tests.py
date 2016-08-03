from selenium import webdriver as wd

import unittest

class BaseFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = wd.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


class NewUserSignUpTest(BaseFunctionalTest):
    def test_new_user_can_sign_up_for_and_sign_in_to_the_service(self):
        # Jeremy heard about a cool new To-Do list application and, being
        # the organizational genius he is, he decides to check it out.
        self.browser.get('localhost:8080')

        # Once the page is loaded, he sees a link that says 'Sign Up' and
        # one that says 'Sign In'. He clicks on the 'Sign Up' link.
        signup_link = self.browser.find_element_by_link_text('Sign Up')
        self.assertIsNotNone(signup_link)

        signin_link = self.browser.find_element_by_link_text('Sign In')
        self.assertIsNotNone(signin_link)

        signup_link.click()

        # Then, he is redirected to the 'Sign Up' page on which he is
        # presented with a text box that asks for him to specify an email
        # address, another asking for a username, a two fields in which he
        # can enter and confirm a password.

        # He enters the following information and submits the form:
        # email    - 'jeremy.white.123@gmail.com'
        # username - 'grneggs'
        # password - 'sp@m'

        # He is redirected to his new profile page where he sees an area
        # that would contain his to-do lists - currently it says 'You do
        # not have any lists, yet. Create one now!'. He also sees a link
        # at the top of the page that reads 'Sign Out'.

        # Satisfied with his new account, and his nifty profile page he
        # signs out and goes to pick pick up his kids.
        self.fail('Finish the test!')

