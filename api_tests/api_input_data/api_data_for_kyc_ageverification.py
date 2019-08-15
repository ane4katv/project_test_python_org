#This is input data file for api_kyc_AgeVerification test

headers = {"Content-Type":"application/json",
			"Ocp-Apim-Subscription-Key":"f09bd683ca1d490a907717e87ca001fb"		
}

body_for_post = {  
   "Request":{  
      "CustomerID":1,
      "CustomerRequestID":2333115,
      "KYCTopic":"AgeVerification",
      "RegulationType":"UK",
      "CasinoID":4,
      "PlayerID":"45612356"
   },
   "Data":{  
      "FirstName":"Leigh",
      "LastName":"Selby",
      "Building":"",
      "Street":"36 Edward Road",
      "City":"",
      "PostCode":"DN212QR",
      "CountryCode":"GB",
      "Email":"leighselby21@gmail.com",
      "DOB":"21/05/1988"
   }
}

# body_for_post_string_customer_id = {  
#    "Request":{  
#       "CustomerID":"1",
#       "CustomerRequestID":2333115,
#       "KYCTopic":"AgeVerification",
#       "RegulationType":"UK",
#       "CasinoID":4,
#       "PlayerID":"45612356"
#    },
#    "Data":{  
#       "FirstName":"Leigh",
#       "LastName":"Selby",
#       "Building":"",
#       "Street":"36 Edward Road",
#       "City":"",
#       "PostCode":"DN212QR",
#       "CountryCode":"GB",
#       "Email":"leighselby21@gmail.com",
#       "DOB":"21/05/1988"
#    }
# }


body_for_post_string_customer_id = body_for_post["Request"]["CustomerID"] = str(body_for_post["Request"]["CustomerID"])
body_for_post_string_customer_request_id = body_for_post["Request"]["CustomerRequestID"] = str(body_for_post["Request"]["CustomerRequestID"])
body_for_post_string_regulation_type_id = body_for_post["Request"]["RegulationType"] = 111
body_for_post_string_casino_id = body_for_post["Request"]["CasinoID"] = str(body_for_post["Request"]["CasinoID"])
body_for_post_player_id = body_for_post["Request"]["PlayerID"] = str(body_for_post["Request"]["PlayerID"])
