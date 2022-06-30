PeanutButterCup =  {
        "introduced" : 1928,
        "ingredients" : ["cocolate", "peanut butter"],
        "owner" : "The Hershey Company",
        "country" : "USA",
        "tasty" : True
        }


PeanutButterCup["color"] = "brown"
counter = 1
choices = {}

for key in PeanutButterCup.keys():
    print(f"{counter}. {key}")
    choices[f"{counter}"] = key
    counter += 1

choice = input("choose a key by it's associated number: ")


if (counter < 2 or int(choice) < 1 or int(choice) > (counter-1)):
    print("invalid input")
else:
    key = choices[f"{choice}"]
    print(f"The information for your choice is: {PeanutButterCup[key]}")
