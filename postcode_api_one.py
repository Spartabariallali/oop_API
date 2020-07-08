import requests
import json

post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_code_req.status_code)
# print(post_code_req.content)
# print(type(post_code_req.content))
# print(post_code_req.headers)
# print(post_code_req)
# print(post_code_req.headers)
# print(type(post_code_req.headers))


class Live_Web_StatusCode:
    def check_status_code():
        website = input("please enter a url you want to verify: \n")
        webstatus = (requests.get(website)).status_code
        if webstatus:
            print("succes")
        elif webstatus== 400:
            print("sorry page unavaiable")
        else:
            pass

check1 = Live_Web_StatusCode
check1.check_status_code()


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



# C.R.U.D 

# create - read - update - delete - four basic databse operations 







