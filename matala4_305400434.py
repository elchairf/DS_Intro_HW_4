# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:49:45 2022

@author: Elchai Refoua
"""
#0ld version
#דרך 1 עם שומרי מקום
#address="Ariel University, Ariel,Israel"
#api_keyo= 'AIzaSyB9X33i68j-haug-oGhl2FZC0UgfUaJ7N0'

#url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(address,api_key) 
#להעתק אקספשיון כתבה יפה ממש                 
#response = requests.get(url).json()#שומרי מקום
#print(type(response))#חוזר לי דיקשיונרי מה שחוזר מגוגל במעבר לפייתון הופך לדישיונרי

#
#destsfile = open(r'C:\Users\User\Desktop\dests.txt')

#serviceurl="https://maps.googleapis.com/maps/api/distancematrix/json?address=%s&key=%s"%(address  ,api_key)  
#parms = dict() #הגדרנו דיקשיונרי פרם ומכניסים אליו
#parms['origins']='תל אביב'
#parms['destinations'] = 'רומא'
#parms['key'] = api_key
#url = serviceurl + urllib.parse.urlencode(parms)#חוקי עכשיו


import math
import requests
import urllib
file = open(r'C:\Users\User\Desktop\dests.txt')
print(file)


#חלק 1

address ="Ariel University,Ariel,Israel"
api_key ='AIzaSyCb0NwtqBtuVdsR5bVijaOrqIKYSNtPBXA'
#הוזן בקלאוד ויש 2 אי פי איי

            # the geocode code that sucsses to get the data but not the content in Python
def get_location(api_key, address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(address,api_key)
    #print(url)
    try:
        response = requests.get(url)
        #print(type(response))
        if response.status_code == 200:
            response = response.json()
            #print(response)
            #print(type(response))
            lati = response['results'][0]['geometry']['location']['lat']
            long = response['results'][0]['geometry']['location']['lng']
            #print(lati,long)
            #print(type(res))
    except Exception as e:
        print(f"{e}")
    return['long:',long,'latitude:',lati]

# חלק 2

def get_time(api_key,destinations):
    parms = dict()
    parms['origins']='Jerusalem'
    parms['destinations'] = destinations
    parms['key'] = api_key
    serviceurl="https://maps.googleapis.com/maps/api/distancematrix/json?"
    url = serviceurl + urllib.parse.urlencode(parms)
    #print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            dist = response['rows'][0]['elements'][0]['distance']['value']/1000
            durat =response['rows'][0]['elements'][0]['duration']['value']
            hours = math.floor(durat/3600)
            mins = (durat%3600)/60
            #print(dist,durat)
            #print(hours, mins)
            return('km',dist,'hours:',hours,'minutues:',mins)
    except Exception as e:
            print(f"{e}")
            
            
file = open(r'C:\Users\User\Desktop\dests.txt')
dictionary = {}
for line in file:
    time = get_time(api_key,line)
    location =  get_location(api_key, line)

    dictionary[line] = (time,location)
print(dictionary)


# מיון הגדולים ביותר 


# biggest =0,0,0
# biggest_cities="","",""
# for city in dictionary :
#     if city[1] > biggest[0]:
#         biggest.insert(city[1])
#         biggest.pop[3]
#         biggest_cities.insert(city)
#         biggest_cities.pop[3]
#
#     elif city[1] > biggest[1]:
#         biggest.insert(1,city[1])
#         biggest.pop[3]
#         biggest_cities.insert(1,city)
#         biggest_cities.pop[3]
#     elif city[1] > biggest[2]:
#         biggest.insert(2, city[1])
#         biggest.pop[3]
#         biggest_cities.insert(2, city)
#         biggest_cities.pop[3]
# print(biggest[:3])















