import os
import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

class Driver:
    def getDriverMethod(self):

        # TO start the appium server through script
        appium_service = AppiumService()
        print(appium_service)

        appium_service.start()


       # Get the directory of the current script
        current_dir = os.path.dirname(__file__)

        # Construct the path to the 'app' directory relative to the current script
        app_dir = os.path.join(current_dir, '..', 'app')

        # Normalize the path to eliminate any redundant separators or up-level references
        app_dir = os.path.abspath(app_dir)

        # Construct the full path to the 'weddingkart.apk' file
        file_path = os.path.join(app_dir, 'weddingkart.apk')

        print(f"The path to the APK file is: {file_path}")

        #Desired Capabilities

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '15'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['app'] = file_path
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['autoGrantPermissions'] = 'true'
        options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

        return driver

    def getremoteServer(self):
        BROWSERSTACK_USERNAME = "chinmayiavinash_ieWEJj"
        BROWSERSTACK_ACCESS_KEY = "wbgNjAo29YqscMEoH8Pp"

        # BrowserStack remote URL
        BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

        # Desired Capabilities for Android Testing
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14.0"  # Adjust based on your needs
        options.device_name = "Samsung Galaxy S24"
        options.automation_name = "UiAutomator2"
        options.auto_grant_permissions="true"

        # 📌 Use an uploaded app (Upload your app to BrowserStack and get the app URL)
        options.app = "bs://172f16ef7688cb5143f4c57ca9f44219140d5c07"  # Replace with your BrowserStack app URL

        # ✅ Initialize WebDriver
        driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

        # ✅ Test Actions (Modify as needed)
        driver.implicitly_wait(10)
        print("Connected to BrowserStack successfully!")

        return driver







