travel_log = {
    "France": {
        "cities_visited":  ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# for country in travel_log:
#     test = travel_log[country]
#     print(f"Country: {country}")
#     for key, value in test.items():
#         print(f"Key: {key} Value: {value}")

travel_list_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

for dic in travel_list_log:
    [Country, Cities_Visited, Total_Visits] = dic.keys()
    country = dic[Country]
    cities_visited = dic[Cities_Visited]
    total_visits = dic[Total_Visits]

    print(f"Country: {country} Cities Visited: {cities_visited} Total Visits: {total_visits}")

# print(travel_log)