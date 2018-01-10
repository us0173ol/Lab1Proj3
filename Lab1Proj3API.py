#api
import requests
import os
import json

#set ZIP_KEY=6L5Dv9LWOV7VrqVeKk8H3boogJ7ieLFA6av8zk877PzNSA8a3ddm4jtRZtGhctit

#key = os.environ['ZIP_KEY']
base_url = 'https://www.zipcodeapi.com/rest/6L5Dv9LWOV7VrqVeKk8H3boogJ7ieLFA6av8zk877PzNSA8a3ddm4jtRZtGhctit/distance.json/'
zip_code1 = input("Please enter the first zip code.")
zip_code2 = input("Please enter the second zipcode to determine distance between the two.")
units = 'mile'
params = {'zip_code1' : zip_code1, 'zip_code2' : zip_code2, 'units' : units}
#units = input("miles or km")
#    if units == miles:
#        units = mile
#    if units == km:
#        units = km
#data = requests.get('https://www.zipcodeapi.com/rest/6L5Dv9LWOV7VrqVeKk8H3boogJ7ieLFA6av8zk877PzNSA8a3ddm4jtRZtGhctit/distance.json/',zip_code1,'/',zip_code2,'/mile')
data = requests.get(base_url, params)


print(data)
