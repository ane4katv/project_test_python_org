from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random
#from locators.login_locators import *  # НУЖНО ИЗМЕНЯТЬ ЛОКАТОРЫ
from functions import *
from locators.login_locators import *


class LoginPage_2:
	def __init__(self, LOGIN_URL, LOGOUT_URL, LOGIN, PASSWORD):
		self.LOGIN_URL = LOGIN_URL
		self.LOGOUT_URL = LOGOUT_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD

	def login(self, driver):
		driver.get(self.LOGIN_URL)
		wait_clickable(driver, SIGN_IN_LOCATOR)
		send_keyz(driver, LOGIN_FIELD, self.LOGIN)
		send_keyz(driver, PASSWORD_FIELD, self.PASSWORD)
		wait_n_click(driver, MAKE_LOGIN_BUTTON)
		wait_clickable(driver, SIGNIN_LOGOUT_MESSAGE)
		# sign_in_message = driver.find_element(SIGNIN_LOGOUT_MESSAGE).text
		# assert sign_in_message.split()[0] == "Successfully"

