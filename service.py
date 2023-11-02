import getpass
# from . import constants as c
import constants as c
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(driver, email=None, password=None, cookie = None, timeout=10):
  
    driver.get("https://www.linkedin.com/login")  
    email_elem = driver.find_element(By.ID,"username")
    email_elem.send_keys(email)
  
    password_elem = driver.find_element(By.ID,"password")
    password_elem.send_keys(password)
    password_elem.submit()
  
    # if driver.current_url == 'https://www.linkedin.com/checkpoint/lg/login-submit':
    #     remember = driver.find_element(By.ID,c.REMEMBER_PROMPT)
    #     if remember:
    #         remember.submit()
  
    # element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, c.VERIFY_LOGIN_ID)))



  
