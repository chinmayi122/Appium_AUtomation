from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Your BrowserStack credentials
BROWSERSTACK_USERNAME = "chinmayiavinash_ieWEJj"
BROWSERSTACK_ACCESS_KEY = "wbgNjAo29YqscMEoH8Pp"



# BrowserStack remote URL
BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Set browser options
chrome_options = Options()
chrome_options.browser_version = "latest"
chrome_options.platform_name = "Windows 10"
chrome_options.set_capability("browserstack.selenium_version", "4.10.0")  # Adjust version if needed

# Start WebDriver session
driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, options=chrome_options)

# Test: Open Google and search something
driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("BrowserStack Selenium Test")
search_box.send_keys(Keys.RETURN)

print("Test completed successfully!")

# Quit driver
driver.quit()

