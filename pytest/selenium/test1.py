import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome() 


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(50)
print("\n\n web opend\n\n")

username_field = driver.find_element("name","username")
password_field = driver.find_element("name","password")
print("\n\n field found\n\n")


#Username:- entering and checking the keys entered is currect or wrong
expected= "Admin"
username_field.send_keys(expected)

actual = username_field.get_attribute("value")
if actual == expected:
    print("Username entered correctly")
else:
    print("Username entered incorrectly")
    
#Password:- entering and checking the keys entered is currect or wrong

expected1= "adminS"

password_field.send_keys(expected1)

actual1 = password_field.get_attribute("value")
if actual1 == expected1:
    print("password entered correctly")
else:
    print("Password entered incorrectly")
    

print("\n\n keys entered\n\n")

password_field.send_keys(Keys.RETURN) 


if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
    print("login failed")
else:
    print("login successful")
    
driver.implicitly_wait(50)