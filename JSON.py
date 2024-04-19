import json
content = {"name": "Arvind", "age": 15}
with open("something.json", "w") as file:
   json.dump(content, file, indent=2) 

