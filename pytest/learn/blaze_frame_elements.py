from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

def selectionpage(fromport, toport):
    driver.implicitly_wait(10)
    driver.get("https://blazedemo.com/")
    from_field = Select(driver.find_element("name","fromPort"))
    from_field.select_by_value(fromport)
    to_field = Select(driver.find_element("name","toPort"))
    to_field.select_by_value(toport)
    submit = driver.find_element("xpath", "/html/body/div[3]/form/div/input")
    submit.send_keys(Keys.ENTER)

def select_flight(path):
    flight_selection = driver.find_element("xpath", path)
    flight_selection.send_keys(Keys.ENTER)

def coustomer_id():
    p_name = driver.find_element("id", "inputName").send_keys("efdrgtbnh")
    p_adress = driver.find_element("id", "address").send_keys("rftgvbd")
    p_city = driver.find_element("id", "city").send_keys("ftgh")
    p_state = driver.find_element("id", "state").send_keys("tgbhdsr")
    p_zipcode = driver.find_element("id", "zipCode").send_keys("gbhnftsegv")
    p_cardtype = Select(driver.find_element("name", "cardType"))
    p_cardtype.select_by_value("visa")
    p_cardnum = driver.find_element("id", "creditCardNumber").send_keys("fgdbhry54ret")
    p_cMonth = driver.find_element("id", "creditCardMonth").send_keys("gbveythrs")
    p_cYear = driver.find_element("id", "creditCardYear").send_keys("ge")
    p_cName = driver.find_element("id", "nameOnCard").send_keys("rtfge")
    remember = driver.find_element("id", "rememberMe")
    remember.send_keys(Keys.ENTER)

    expected = "https://blazedemo.com/confirmation.php"
    current = driver.current_url

    if current== expected:
        print("done")
    else:
        assert current == expected, "Purchase fail"
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_file = f"failure_{timestamp}.png"
        driver.save_screenshot(screenshot_file)


    driver.quit()





# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# def selectionpage(fromport,toport):
#     driver.implicitly_wait(10)
#     driver.get("https://blazedemo.com/")
#     from_field= Select(driver.find_element("name", "fromPort"))
#     from_field.select_by_value(fromport)
#     to_field=Select(driver.find_element("name", "toPort"))
#     to_field.select_by_value(toport)
#     submit= driver.find_element("xpath","/html/body/div[3]/form/div/input")
#     submit.send_keys(Keys.ENTER)


# def select_flight(path):
#     flight_selection=driver.find_element("xpath",path)
#     flight_selection.send_keys(Keys.ENTER)


# def coustomer_id():
#     p_name=driver.find_element("id","inputName").send_keys("efdrgtbnh")
#     p_adress= driver.find_element("id","address").send_keys("rftgvbd")
#     p_city= driver.find_element("id","city").send_keys("ftgh")
#     p_state=driver.find_element("id","state").send_keys("tgbhdsr")
#     p_zipcode =driver.find_element("id","zipCode").send_keys("gbhnftsegv")
#     p_cardtype= Select(driver.find_element("name","cardType"))
#     p_cardtype.select_by_value("visa")
#     p_cardnum=driver.find_element("id","creditCardNumber").send_keys("fgdbhry54ret")
#     p_cMonth= driver.find_element("id","creditCardMonth").send_keys("gbveythrs")
#     p_cYear= driver.find_element("id","creditCardYear").send_keys("ge")
#     p_cName= driver.find_element("id","nameOnCard").send_keys("rtfge")
#     remember=driver.find_element("id","rememberMe")
#     remember.send_keys(Keys.ENTER)
#     # submit=driver.find_element("value","Purchase Flight")
#     # submit.send_keys(Keys.ENTER)
#     expected="https://blazedemo.com/confirmation.php"
#     current= driver.current_url
    
#     assert current==expected,"purchase fail"
#     import datetime
#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     screenshot_file = f"failure_{timestamp}.png"
#     driver.save_screenshot(screenshot_file)
        
#     # else:
#     #     print("purchase conform")
#     driver.quit