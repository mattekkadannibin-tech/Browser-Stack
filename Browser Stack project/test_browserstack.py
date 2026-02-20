from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_elpais():
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "ElPais Test",
        "projectName": "BrowserStack Project",
        "buildName": "ElPais Build",
        "userName": "mattekkadannibin_PeQRWC",
        "accessKey": "auErsxbwsYiXK8yb6rFf",
        "debug": True,
        "networkLogs": True,
        "consoleLogs": "info"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://elpais.com/opinion/")
    time.sleep(5)

    print("Page Title:", driver.title)

    session_id = driver.session_id
    print(f"BrowserStack session URL: https://automate.browserstack.com/sessions/{session_id}.json")

    driver.quit()
