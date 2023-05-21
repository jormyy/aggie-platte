import json

def WriteTojson(nutrition):
    '''
        writes to json file
    '''
    file = open("food.json", "w")
    file.write(json.dumps(nutrition))
    file.close