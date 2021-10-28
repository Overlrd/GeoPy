import phonenumbers
from number import my_number
from number import key
from phonenumbers import geocoder
import folium
import webbrowser as wb

nb=phonenumbers.parse(my_number)
nb_location =geocoder.description_for_number(nb, "en")
print(nb_location)

##get service provider

from phonenumbers import carrier

service_provider =phonenumbers.parse(my_number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder= OpenCageGeocode(key)

query =str(nb_location)

results =geocoder.geocode(query)
#print(results)
import json
with open("infos.txt", "w") as file:
	file.write(json.dumps(results))
file.close()

lat =results[0]["geometry"]["lat"]
lng =results[0]["geometry"]["lng"]
print(lat,lng)

Map =folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=nb_location).add_to((Map))

Map.save("location.html")
wb.open("location.html")
print("Done")