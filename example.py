import json



def readInvalidDataFromJson():
    file = open("data/invalidLogin.json") 
    data = json.load(file)
    parameter = []

    for user in data['users']:
        username = user["username"]
        password = user["password"]
        parameter.append((username,password))

    print(parameter)

readInvalidDataFromJson()