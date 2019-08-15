import pytest
from api_input_data.api_data_for_kyc_ageverification import *

pytestmark = [pytest.mark.nondestructive]



# CRUD

# CREATE TABLE ...
# INSERT

# UPDATE

# DELETE


# GET - Read 

# POST - UPDATE/CREATE

# PATCH - UPDATE

# PUT  - UPDATE

# DELETE - DELETE




#Launch line: pytest test_api_kyc_AgeVerification.py -v -s --disable-pytest-warnings

#POSITIVE TEST CASES
#This test makes default request(POST) with correct input data and url
def test_post_request_default(api):
	response = api.post('', headers=headers, json=body_for_post, verify=False)
	assert response.status_code == 200


#NEGATIVE TEST CASES
#TESTING METHODS, WHICH NOT ALLOWED
#This test makes GET request with correct url, but without any data (no headers, no body, no parameters)
def test_get_request_without_any_data(api):
	response = api.get('', verify=False)
	assert response.status_code == 404

#This test makes POST request with correct url, but without any data (no headers, no body, no parameters)
def test_post_request_without_any_data(api):
	response = api.post('', verify=False)
	assert response.status_code == 401

#This test makes PUT request with correct url, but without any data (no headers, no body, no parameters)
def test_put_request_without_any_data(api):
	response = api.put('', verify=False)
	assert response.status_code == 404

#This test makes PATCH request with correct url, but without any data (no headers, no body, no parameters)
def test_patch_request_without_any_data(api):
	response = api.patch('', verify=False)
	assert response.status_code == 404

#This test makes DELETE request with correct url, but without any data (no headers, no body, no parameters)
def test_delete_request_without_any_data(api):
	response = api.delete('', verify=False)
	assert response.status_code == 404


#TESTING METHODS WITH DIFFERENT INPUT DATA
#This test makes default request(POST) with correct url and input data, except CustomerID data type -> string (should be integer)
def test_post_request_customer_id_as_string(api):
	response = api.post('', headers=headers, json=body_for_post_string_customer_id, verify=False)
	assert response.status_code == 400

#This test makes default request(POST) with correct url and input data, except CustomerRequestID data type -> string (should be integer)
def test_post_request_customer_request_id_as_string(api):
	response = api.post('', headers=headers, json=body_for_post_string_customer_request_id, verify=False)
	assert response.status_code == 400

#This test makes default request(POST) with correct url and input data, except RegulationType data type -> integer (should be string)
def test_post_request_regulation_type_as_integer(api):
	response = api.post('', headers=headers, json=body_for_post_string_regulation_type_id, verify=False)
	assert response.status_code == 400

#This test makes default request(POST) with correct url and input data, except CasinoID data type -> string (should be integer)
def test_post_request_casino_id_as_string(api):
	response = api.post('', headers=headers, json=body_for_post_string_casino_id, verify=False)
	assert response.status_code == 400

#This test makes default request(POST) with correct url and input data, except PlayerID data type -> string (should be integer)
def test_post_request_player_id_as_string(api):
	response = api.post('', headers=headers, json=body_for_post_player_id, verify=False)
	assert response.status_code == 400














