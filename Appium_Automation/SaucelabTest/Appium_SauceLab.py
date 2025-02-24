import os
import time


from appium import webdriver, options
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.remote.client_config import ClientConfig

# Your Sauce Labs Credentials
SAUCE_USERNAME = "oauth-chinmayiavinash58-293c6"
SAUCE_ACCESS_KEY = "6305cd3e-781a-46a4-96e2-c8e9628c94bc"

print(f"Username: {SAUCE_USERNAME}")
print(f"Access Key: {SAUCE_ACCESS_KEY}")


#SAUCE_URL = "https://ondemand.us-west-1.saucelabs.com/wd/hub"
SAUCE_URL = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.us-west-1.saucelabs.com/wd/hub"


options = UiAutomator2Options()
options.platformName= "Android"
options.platformVersion= "14.0"# Adjust based on your device
options.deviceName= "Android GoogleAPI Emulator"  # Choose a supported device
options.browserName= "Chrome"  # Use "Chrome" for web tests or app details for native testing
options.automationName= "UiAutomator2"
options.app= "storage:filename=weddingkart.apk"

# Initialize WebDriver with secure authentication
driver = webdriver.Remote(command_executor=SAUCE_URL, options=options)

# Test run
print("Connected to Sauce Labs successfully!")

# run commands and assertions
driver.get("https://www.saucedemo.com")
title = driver.title
titleIsCorrect = "Swag Labs" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script('sauce:job-result=' + jobStatus)
driver.quit()