from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import random

class LoginPage:
	def __init__(self, LOGIN_URL, LOGOUT_URL, LOGIN, PASSWORD):
		self.LOGIN_URL = LOGIN_URL
		self.LOGOUT_URL = LOGOUT_URL
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		
		
	def login(self, driver):
		driver.implicitly_wait(10) # NEED TO TALK
		driver.get(self.LOGIN_URL)
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/form/button')))
		login_field = driver.find_element(By.XPATH, '//*[@id="id_login"]')
		password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')
		login_field.send_keys(self.LOGIN)
		password_field.send_keys(self.PASSWORD)
		make_login = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/button').click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/div[1]/p')))
		sign_in_message = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/p').text
		assert sign_in_message.split()[0] == "Successfully"
		
	def logout(self, driver):
		driver.get(self.LOGOUT_URL)
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/form/button')))
		make_logout = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/button').click()
		sign_out_message = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/p').text
		assert sign_out_message == "You have signed out."

		
