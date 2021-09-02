travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country: str, timesVisit: int, cities: list):
    travel = {
        "country": country,
        "visits": timesVisit,
        "cities": cities
    }

    print(f"""
    You've visited {country} {timesVisit} times.
    You've been to {cities[0]} and {cities[1]}
    """)

    travel_log.append(travel)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

