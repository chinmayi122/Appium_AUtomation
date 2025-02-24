import time
import unittest

from pages.LoginPage import LoginPage
from pages.WeddingPage import  WeddingPage
import pytest


@pytest.mark.usefixtures("beforeClass","beforeMethod")
class CrudOperations_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.wp = WeddingPage(self.driver)




    @pytest.mark.run(order=2)
    def test_createwedding(self):
        #ENTER PHONE NUMBER
        self.lp.enterPhoneNumber()

        #CLICK ON CONTINUE BUTTON
        self.lp.continueButton()
        time.sleep(2)

        #ENTER THE OTP
        self.lp.enterOtp()


        #CLICK ON VERIFY AND PROCEED
        self.lp.verifyAndProceed()
        time.sleep(2)

        #CLICK ON CREATE WEDDING BUTTON IN THE HOMEPAGE
        self.wp.createWedding()


        #CLICK ON SELECT YOUR ROLE
        self.wp.yourRole()

        #CLICK ON EVENT MANAGER IN THE DROPDOWN
        self.wp.selectYourRole()

        #CLICK ON DONE BUTTON
        self.wp.doneBUtton()


        #CLICK ON WEDDING DATE
        self.wp.WeddingDate()


        #SELECT A WEDDING DATE
        self.wp.selectWeddingDate()

        #CLICK ON OK BUTTON
        self.wp.okBUtton()
        time.sleep(3)

        #SEND TEXT IN THE BRIDES NAME HOLDER
        '''self.wp.bridesNameClick()
        time.sleep(5)'''

        self.wp.bridesName()
        time.sleep(3)


        self.wp.groomsName()
        time.sleep(3)




        ''''#SEND THE TEXT IN THE GROOMS NAME HOLDER
        self.wp.groomsName()
        time.sleep(3)

        #CLICK ON CREATE THE WEDDING IN THE CREATE WEDDING PAGE
        self.wp.createWeddingButton()

        #CHECK IF WEDDING IS CREATED
        self.wp.weddingCreated()'''









