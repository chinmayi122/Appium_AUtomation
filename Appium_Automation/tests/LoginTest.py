import time
import unittest

from base.BasePage import BasePage
from pages.LoginPage import  LoginPage
import pytest
from utilities.CustomLogger import CustomLogger as cl


@pytest.mark.usefixtures("beforeClass","beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp=LoginPage(self.driver)
        self.bp=BasePage(self.driver)


    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.enterPhoneNumber()

        self.lp.continueButton()

        self.lp.enterOtp()

        self.lp.verifyAndProceed()

        self.lp.hamburgerMenu()

        self.lp.logout()












