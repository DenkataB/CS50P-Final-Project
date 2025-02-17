from datetime import datetime
import pytz
import requests
import re
import json
import sys
import pyfiglet

def main():
    print(pyfiglet.figlet_format("The Instant Traveler"))

    api_key, url, arrival_airport, departure_airport = get_info()

    params = {
        "access_key": api_key,
        "dep_iata": get_iata_code(departure_airport),
        "arr_iata": get_iata_code(arrival_airport),
        "limit": 10
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "data" in data:
        flights = data["data"]
        if flights:
            print()
            print(f"Flights from {get_city_name(departure_airport)} to {get_city_name(arrival_airport)}:")
            any_flights = False

            for flight in flights:
                if check_time(flight):
                    any_flights = True
                    print()
                    print(f"Flight Number: {flight['flight']['iata']}")
                    print(f"Airline: {flight['airline']['name']}")
                    print(f"Departure Airport: {flight['departure']['airport']}")
                    print(f"Departure Date: {format_schedule(flight['departure']['scheduled'])} local time")
                    print(f"Arrival Airport: {flight['arrival']['airport']}")
                    print(f"Arrival Date: {format_schedule(flight['arrival']['scheduled'])} local time")
                    print("_" * 50)

            if not any_flights:
                print("No remaining flights for this route today")
        else:
            print("No flights for this route")
    else:
        print("Failed to recieve flight info")

def get_info():
    api_key = "268893d0a04ecce42df2561b24765bab"
    url = f"http://api.aviationstack.com/v1/flights"
    arrival_airport = input("Where do you want to go today? ").strip()
    departure_airport = input("Where do you depart from? ").strip()
    return api_key, url, arrival_airport, departure_airport

def format_schedule(date):
    matches = re.search(r"^(.+)-(.+)-(.+)T(\d{2}:\d{2}).+$", date)
    scheduled_date = f"{matches.group(3)}/{matches.group(2)}/{matches.group(1)}"
    return f"{scheduled_date} at {matches.group(4)}"

def get_iata_code(inp):
    with open("cities.json", "r") as file:
        cities = json.load(file)

    if re.search(r"^([a-zA-Z]{3})$", inp):
        try:
            for city in cities:
                if city["iata_code"].lower() == inp.lower():
                    return city["iata_code"]
        except AttributeError:
            sys.exit("City not found")
    else:
        for city in cities:
            if city["city_name"].lower() == inp.lower():
                return city["iata_code"]
        else:
            sys.exit("City not found")

def get_city_name(inp):
    with open("cities.json", "r") as file:
        cities = json.load(file)

    if re.search(r"^([a-zA-Z]{3})$", inp):
        try:
            for city in cities:
                if city["iata_code"].lower() == inp.lower():
                    return city["city_name"]
        except AttributeError:
            sys.exit("Airport not found")
    else:
        for city in cities:
            if city["city_name"].lower() == inp.lower():
                return city["city_name"]
        else:
            sys.exit("Airport not found")

def check_time(data):
    timezone = pytz.timezone(data["departure"]["timezone"])
    departure_arrea_current_time = datetime.now(timezone)

    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):.+$", data["departure"]["scheduled"])
    year = int(matches.group(1))
    month = int(matches.group(2))
    day = int(matches.group(3))
    hour = int(matches.group(4))
    minutes = int(matches.group(5))
    departure_time = timezone.localize(datetime(year, month, day, hour, minutes))

    return departure_arrea_current_time < departure_time

if __name__ == "__main__":
    main()
