import requests
import json

post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_code_req.status_code)
# first iteration
# if post_code_req.status_code == 200:
#     print("success")
# elif post_code_req.status_code == 404:
#     print(" sorry page unavailable")

# second iteration 
# if post_code_req.status_code:
#     print("success")
# elif post_code_req.status_code == 404:
#     print(" sorry page unavailable")

# Third iteration - create same functionality with oop (class and method):

class Check_Status:
    def check_status_code():
        if post_code_req.status_code:
            print("succes")
        elif post_code_req.status_code == 400:
            print("sorry page unavaiable")


check1 = Check_Status
check1.check_status_code()