from appium.options.android import UiAutomator2Options
from selenium import webdriver


# Your BrowserStack credentials
BROWSERSTACK_USERNAME = "chinmayiavinash_ieWEJj"
BROWSERSTACK_ACCESS_KEY = "wbgNjAo29YqscMEoH8Pp"



# BrowserStack remote URL
BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Desired Capabilities for Android Testing
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "13.0"  # Adjust based on your needs
options.device_name = "Samsung Galaxy S23"
options.automation_name = "UiAutomator2"

# 📌 Use an uploaded app (Upload your app to BrowserStack and get the app URL)
options.app = "bs://172f16ef7688cb5143f4c57ca9f44219140d5c07"  # Replace with your BrowserStack app URL

# ✅ Initialize WebDriver
driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

# ✅ Test Actions (Modify as needed)
driver.implicitly_wait(10)
print("Connected to BrowserStack successfully!")

