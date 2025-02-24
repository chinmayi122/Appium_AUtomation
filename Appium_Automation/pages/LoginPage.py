import time

from base.BasePage import BasePage
from utilities.CustomLogger import CustomLogger as cl


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    #Locator Values in Login and sign up Pages

    _enterPhoneNumer="//android.widget.EditText"  #xapth
    _continueButton="//android.widget.Button[@content-desc='Continue']"
    _enteringOtp="//android.widget.EditText"
    _verifyAndProceed="//android.widget.Button[@content-desc='Verify and Proceed']"
    _hamburgerMenu="//android.widget.Button[@content-desc='Open navigation menu']"
    _logout="//android.widget.Button[@content-desc='Logout']"




    def enterPhoneNumber(self):
        self.SendKeys("9999999999",self._enterPhoneNumer,"xpath")
        time.sleep(2)



    def continueButton(self):
        self.ClickElement(self._continueButton,"xpath")


    def enterOtp(self):
        self.SendKeys("1234",self._enteringOtp,"xpath")



    def enterOtp2(self):
        self.SendKeys("123467", self._enteringOtp, "xpath")


    def verifyAndProceed(self):
        self.ClickElement(self._verifyAndProceed,"xpath")

    def hamburgerMenu(self):
        self.ClickElement(self._hamburgerMenu,"xpath")

    def logout(self):
        self.ClickElement(self._logout,"xpath")


