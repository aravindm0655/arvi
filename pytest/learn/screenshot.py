
def loginpage(username, password):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    global login 
    global current
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_field = driver.find_element("name", "username")
    password_field = driver.find_element("name", "password")
    submit= driver.find_element("id","submit")
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit.send_keys(Keys.ENTER)
    driver.implicitly_wait(30)
    login="https://practicetestautomation.com/practice-test-login/"
    current = driver.current_url
    


def test_url():
    assert login==current, "login failed"
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_file = f"failure_{timestamp}.png"
    driver.save_screenshot(screenshot_file)
