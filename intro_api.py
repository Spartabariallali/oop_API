# Application Programming Interface 

# what is an API? and why is it used?
# used as medium to connect between programmes 

# module called requests that interacts with web-based APIs

# pip install requests 

# http/https requests helps us obtain data from the web 
# check the response code - 200 - 400 - 404 (page not found)

import requests 

#check the response code - 200 - 400 - 404 (page not found)
response_bbc = requests.get("https://www.bbc.co.uk")
response_facebook = requests.get("https://www.facebook.com")

# print(response_bbc.status_code)
# print(response_bbc.headers) #
# print(response_bbc.content) #

# print(type(response_facebook.status_code))
# print(type(response_facebook.headers))


# response_bbc = requests.get("https://www.bbc.co.uk")
# # receive a response code and if == 200 print ("success")
# if response_bbc.status_code == 200:
#     print("this website is available")
# # elif != 200 print ("page not found")
# elif response_bbc.status_code != 200:
#     print("page not found")
# # else print ("Something went wrong")   
# else:
#     print("something went wrong")

# 2nd Iteration
# create a function called check_response_code() including all the above

check_status = input(requests.get("please enter a website you would like to access: "))

print(requests.get(check_status))
print(check_status.status_code)


# def check_response_code():
#     if check_status.status_code == 200:
#         print("--->>>this website is available now<<<---")
#         print("https://www.bbc.co.uk")
#     elif check_status.status_code != 200:
#         print("page not found")
#         print("if you would like to access the home page, please click the link below")
#         print("https://www.bbc.co.uk")
#     else:
#         print("something went wrong")


# returns the message with status code





# create a function 



