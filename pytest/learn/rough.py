from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://blazedemo.com/")
from_field = Select(driver.find_element("name", "fromPort"))
from_field.select_by_value("Paris")
to_field = Select(driver.find_element("name", "toPort"))
to_field.select_by_value("Rome")
print("\n\ndgthgnf\n\n")
submit = driver.find_element("xpath", '//input[@value="Find Flights"]')
submit.click
print("click entered")



