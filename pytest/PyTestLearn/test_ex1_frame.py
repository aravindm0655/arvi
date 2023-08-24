from selenium import webdriver
from selenium.webdriver.common.keys import Keys

file=open('cerdentials.txt','r')

def loginpage1():
    global login 
    global current
    global driver 
    credential = file.readline()
    username,password = credential.split(',')
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
        
            

def test_url1():
    if current == login:
        driver.implicitly_wait(10)
        error_message = driver.find_element("id","error")
        errmsg= error_message.get_attribute
        if errmsg != None:
            print("wrong credential")
        else:
            assert "failed"
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_file = f"failure_{timestamp}.png"
            driver.save_screenshot(screenshot_file)







