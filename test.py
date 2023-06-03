import json

my_dict = {
       "name" : "Fran",
       "age" : 44,
       "city": "Lisbon"
}

with open( "my_dict.json", "w") as file:
       json.dump(my_dict, file)

