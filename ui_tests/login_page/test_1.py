import pytest


#REPORTING:
# need to install: pip install pytest-html
# usage pytest filename.py broweser_specification -v -s --html=report.html --self-contained-html

#MARK USAGE
# call mark list (+help): pytest --markers
# call marks in launch line:
# -m critical
# -m "not critical"
# launch all unmarked https://pypi.org/project/pytest-unmarked/
# --unmarked

def test_login(login_model, selenium):
	login_model.login(selenium)


# def test_login_logout(login_model, selenium):
# 	login_model.login(selenium)
# 	login_model.logout(selenium)

# def gns_mark_1():
# 	pass


# @pytest.mark.regression
# def gns_mark_2():
# 	pass

# def anna_mark_3():
# 	pass




