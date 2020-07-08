import requests
import json

post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# print(post_code_req.json())

json_postcode_data = post_code_req.json()

for key in json_postcode_data: #iterate through the keys of the json data (dictionary
       print(key)

# print(json_postcode_data)

# excercise is to fetch data by key value pairs within the dictionary 

for key,value in json_postcode_data.items():  
    print(key,value)


# create a function to return the above values (key:Value) pairs 

class Json_Reader:

    def get_all_values(self, json_postcode_data):

        for key,value in json_postcode_data.items(): # retrieves all key value pairs if there is a nested dictionary it the retrieves the name of the dictionary   
            if type(value) == dict:
                self.get_all_values(value) # 
            else:
                print(key,value, "\n" )

reader = Json_Reader()

reader.get_all_values(json_postcode_data)



class Json_dictionary_sorter:

    def json_reader(self, json_postcode_data):
        
        post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
        json_postcode_data = post_code_req.json()

        for key in json_postcode_data:
            key1 = json_postcode_data.get(key)
            if type(key1) == dict:
                key2 = json_postcode_data['result'].get(key)
                if key2 == dict:
                    for key in json_postcode_data['results']['codes']:
                        print(key, ":", json_postcode_data["results"]["codes"].get(key))
                else:
                    print(key,":",key2)


reader2 = Json_dictionary_sorter()

reader2.json_reader(json_postcode_data)