import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from driver import driver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time



class BasePage:
    log=cl.CustomLogger()

    def __init__(self,driver):
        self.driver=driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType=locatorType.lower()
        element=None
        wait=WebDriverWait(self.driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException
                                                                          ,NoSuchElementException])

        if locatorType=="id":
            element=wait.until(lambda x: x.find_element(AppiumBy.ID,locatorValue))

            return element

        elif locatorType == "class":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.CLASS_NAME,locatorValue))

            return element

        elif locatorType == "des":
            element = wait.until(
               lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % locatorValue))

            return element


        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().index("%d")' % int(locatorValue)))

            return element

        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")' % locatorValue))

            return element

        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorValue)))

            return element

        else:
            self.log().info('Locator Value' + locatorValue + "not found")

        return element

    #To perform some actions on element

    def getElement(self,locatorValue,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.waitForElement(locatorValue,locatorType)
            self.log.info("element found" + locatorType + "with locator value" + locatorValue)

        except:
            self.log.info("element not found" + locatorType + "with locator value" + locatorValue)



        return element

    def ClickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info("Clicking on element with" + locatorType + "with locator value" + locatorValue)

        except:
            self.log.info("Cannot click on the element with" + locatorType + "with locator value" + locatorValue)

        return element

    def SendKeys(self, text , locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info("Send a text with locator type" + locatorType + "with locator value" + locatorValue)

        except:
            self.log.info("Unable to send the text with locator type" + locatorType + "with locator value" + locatorValue)
            self.takeScreenShot(locatorType)


        return element

    def isDisplayed(self,text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.isDisplayed(text)
            self.log.info("Element with" + locatorType + "with locator value" + locatorValue + "isdisplayed")
            return True
        except:
            self.log.info("Element with" + locatorType + "with locator value" + locatorValue + "is not displayed")
            return False

        return element

    def screenShot(self,screenshotName):
        fileName=screenshotName + " " + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory="../screenshots/"
        screenshotPath=screenshotDirectory+fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("screenshot saved to the path: " + screenshotPath)
        except:
            self.log.info("screenshot is not saved to the path: " + screenshotPath)

    def set_implicit_wait(self, seconds=10):
        """Sets an implicit wait for all elements."""
        self.driver.implicitly_wait(seconds)


    def takeScreenShot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text,attachment_type=AttachmentType.PNG)




