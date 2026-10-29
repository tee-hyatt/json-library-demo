import json

library = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "available": True
}

# Write the dictionary to the JSON file
with open("library.json", "w") as file:
    json.dump(library, file, indent=4)

# Read the data from the JSON file
with open("library.json", "r") as file:
    data = json.load(file)

print(data)

# Modify the data
data["available"] = False

# Write the modified data back to the JSON file
with open("library.json", "w") as file:
    json.dump(data, file, indent=4)