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
# 🚨 Do NOT change the code above
# for count, items in enumerate(travel_log):
#     for keys in items:
#         print(travel_log[count][keys])

# index = 0
# while index < len(travel_log):
#     for key in travel_log[index]:
#         print(travel_log[index][key])
#     index += 1


def add_new_country(country_name, places, cities):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = places
    new_country["cities"] = cities
    travel_log.append(new_country)


# print(items)
# # TODO: Write the function that will allow new countries
# to be added to the travel_log
# travel_log.append("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
