animals=[
    {'type':'cat', 'name':'steph', 'age':3},
    {'type':'dog', 'name':'devon', 'age':2},
    {'type':'rhino', 'name':'moe', 'age':8}
]
sort_animals=animals.sort(key=lambda animal: animal["age"])
print("******************************")
print(sort_animals)
sorted_animals=(sorted(animals, key=lambda animal: animal["age"]))
print(sorted_animals)
