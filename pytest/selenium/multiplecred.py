from selenium import webdriver
from selenium.webdriver.common.keys import Keys

result = []
with open('cerdentials.txt', 'r') as file:
    credentials = file.readlines()
  
for credential in credentials:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username, password = credential.split(',')

    username_field = driver.find_element("name", "username")
    password_field = driver.find_element("name", "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    current = driver.current_url

    if current == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
        result.append("test fail")
  
    else:
        result.append("test pass")
    driver.quit()

with open('arv.txt', 'w') as file:
    for item in result:
        file.write(str(item) + '\n')        