# Nesting

# Nesting a Dictionary in list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


def add_new_country(country_visited, times_visited, cities_vistied):
    new_country = {"country": country_visited, "visits": times_visited, "cities": cities_vistied}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
