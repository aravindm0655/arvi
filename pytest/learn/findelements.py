from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://expense-tracker-application-mern.netlify.app/")
class find_e:
    def findelement(type,path):
        global a
        a= driver.find_element((type,path))

class send:
    def sendkeys(data):
        a.send_keys(data)
