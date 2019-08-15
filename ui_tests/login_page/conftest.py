import pytest
# from login_page_object import LoginPage
from login_page_other_approach import LoginPage_2

# Read from file function
def get_data(data):
	return data.split("#")[0]
# Open settings file
f = open("credentials.txt", "r")
#f = open("settings.txt", "r")
lines = f.readlines()
line_1 = get_data(lines[0])
line_2 = get_data(lines[1])
f.close()

#FIXTURES
@pytest.fixture()
def login_model(request):
	fixture = LoginPage_2(line_1, line_2, "nemesis", "123456aA")
	return fixture


@pytest.fixture
def chrome_options(chrome_options):
	chrome_options.add_argument('--log-level=3')
	chrome_options.add_argument('no-sandbox')
	chrome_options.add_argument('--start-maximized')
	return chrome_options




# 2nd APPROACH
# @pytest.fixture()
# def login_model_2(request):
# 	fixture = LoginPage(line_1, line_2, "nemesis", "123456aA")
# 	return fixture
