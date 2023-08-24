from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def loginpage1(username, password):
    global login
    global current 
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://expense-tracker-application-mern.netlify.app/")
    username_field = driver.find_element("xpath", '//input[@type="text"]')
    password_field = driver.find_element("xpath", '//input[@type="password"]')
    submit = driver.find_element("xpath", '//button[@type="submit"]')
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit.send_keys(Keys.ENTER)
    current= driver.current_url
    login = "https://expense-tracker-application-mern.netlify.app/"


def test_url1():
    if current == login:
        driver.implicitly_wait(10)
        error_message = driver.find_element("xpath", '//div[@class="error-message-in-login"]')
        errmsg = error_message.get_attribute("value")
        if errmsg is not None:
            print("wrong credential")
        else:
            assert "failed"
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_file = f"failure_{timestamp}.png"
            driver.save_screenshot(screenshot_file)


    # df = pd.read_excel("credentials.xlsx")
    # for index, row in df.iterrows():
    #     username = row["Username"]
    #     password = row["Password"]
    #     loginpage1(username, password)
