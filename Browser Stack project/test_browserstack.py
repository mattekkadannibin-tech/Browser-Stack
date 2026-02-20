from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_elpais():

    options = webdriver.ChromeOptions()

    # BrowserStack capabilities
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "ElPais Test",
        "userName": "Mattekkadan Nibin",   # your username
        "accessKey": "mattekkadam@123"     # your access key
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://elpais.com/opinion/")
    time.sleep(5)

    print("Title:", driver.title)

    driver.quit()
