capitalCity = {
    "USA" : "wasington DC",
    "killer" : "somone",
}

print(capitalCity.get("USA"))
print(capitalCity.get("killer"))
capitalCity.update({"garmany": "barlin"})
capitalCity.update({"USA" : "new york"})
capitalCity.pop("killer")
capitalCity.popitem()
# capitalCity.clear()

keys = capitalCity.keys()
valiu = capitalCity.values()

print(capitalCity)

print(keys)
print(valiu)