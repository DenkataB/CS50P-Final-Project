import json
import requests

access_key = "c4045a01c8f360b25b149aac2c9f7bf3"
offset = 0
loop = 1

data_json = []

while True:
    url = f"https://api.aviationstack.com/v1/cities?access_key={access_key}&offset={offset}"

    response = requests.get(url)
    data = response.json()

    for entry in data["data"]:
        new_entry = {
            "city_name": entry["city_name"],
            "iata_code": entry["iata_code"],
            "country_iso2": entry["country_iso2"],
            "timezone": entry["timezone"]
        }
        data_json.append(new_entry)
        
    print(f"Loop {loop} done!")
    loop += 1

    offset += 100
    if offset == 10000:
        break

with open("cities.json", "a") as outfile:
    json.dump(data_json, outfile, indent=4)

print("Data has been reformatted and saved to 'cities.json'")
