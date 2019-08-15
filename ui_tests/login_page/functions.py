from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




#FUCTIONS:
# just wait
def wait(driver, locator):
	try:
		WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
	except:
		print (f"Element to wait {locator} is not found")

def wait_clickable(driver, locator):
	try:
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
	except:
		print (f"Element to wait {locator} is not found")

#waits until element will be clickable and click on it
def wait_n_click(driver, locator):
	try: 
		WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator)).click()
	except:
		print (f"Element to click {locator} is not found")

#waits until element will be clickable, sends keywords
def send_keyz(driver, locator, keyz):
	try: 
		WebDriverWait(selenium, 20).until(EC.presence_of_element_located(locator)).send_keys(keyz)
	except:
		print (f"Element to enter value {locator} is not found")
