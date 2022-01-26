import json

# Read json file
def load_json(file_path):
    """
    retrieve high score list json from save file

    Swah Jianoon T01 26th January
    """
    f = open (file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data

# Update or create new save file
def update_json(file_path,data):
    """
    update json high score list in save file. creates new a new file if no file exists.

    Swah Jianoon T01 26th January
    """
    with open(file_path, "w") as jsonFile:
        json.dump(data, jsonFile)
    
