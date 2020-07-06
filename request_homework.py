import requests

response_bbc = requests.get("https://www.bbc.co.uk")

print(response_bbc.status_code)

response_bbc = requests.get("https://www.bbc.co.uk")
# receive a response code and if == 200 print ("success")
if response_bbc.status_code == 200:
    print("this website is available")
# elif != 200 print ("page not found")
elif response_bbc.status_code != 200:
    print("page not found")
# else print ("Something went wrong")   
else:
    print("something went wrong")

response_bbc = requests.get("https://www.bbc.co.uk")

def check_response_code():
    if response_bbc.status_code == 200:
        print("--->>> this website is available now <<<---")
    elif response_bbc.status_code != 200 and response_bbc.status_code == 400:
        print("page not found")
    else:
        pass

check_response_code()



