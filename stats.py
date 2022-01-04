import json


def add_stat(yout=0, inst=0, err=0):
    try:
        dict_stat = read_stats()
    except:
        dict_stat = {
            "yout": 0,
            "inst": 0,
            "err": 0
        }

    dictionary = {
        "yout": yout + int(dict_stat['yout']),
        "inst": inst + int(dict_stat['inst']),
        "err": err + int(dict_stat['err'])
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("stats.json", "w") as outfile:
        outfile.write(json_object)


def read_stats():
    # Opening JSON file
    with open('stats.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return json_object
