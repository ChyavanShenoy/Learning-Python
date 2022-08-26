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


def add_new_country(country_visited, times_visited, cities_visited):
    travel_log.append({"country": country_visited,
                      "visits": times_visited, "cities": cities_visited})


add_new_country("Italy", 5, ["Rome", "Milan", "Naples"])
add_new_country("Spain", 10, ["Madrid", "Barcelona", "Valencia"])
add_new_country("England", 15, ["London", "Liverpool", "Manchester"])
add_new_country("Russia", 25, ["Moscow", "Saint Petersburg", "Novosibirsk"])

print(travel_log)
