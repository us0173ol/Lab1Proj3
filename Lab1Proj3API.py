#api
import requests
import json
#API key from website for requests
zip_key='wkJcjnVyfSih8YNlKFJZsUtzLuFeTlFUG7FkotiE5fZG5aW6NjICvL8Vtv6SHNTr'
#url to send requests to
base_url = 'https://www.zipcodeapi.com/rest/'
#Get input from the user for checking the distance between the zip codes
zip_code1 = input("Please enter the first zip code. ")
zip_code2 = input("Please enter the second zipcode to determine distance between the two. ")
#Figure out the distance in either miles or km
# TODO: error handling for input
units = input("miles or km?")
if units == "miles":
    units = 'mile'
if units == "km":
    units = 'km'
#create the full url to send the request
new_url = base_url+zip_key+'/distance.json/'+zip_code1+'/'+zip_code2+'/'+units
data = requests.get(new_url).json()
print(data)
#TODO: finish up pulling info from the dictionary and displaying
#that info properly
print('-------------------------------------------')
