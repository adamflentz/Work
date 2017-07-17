import sys, json

jsonfile = open(sys.argv[1])
input = json.load(jsonfile)
jsonfile.close()

for item in input:
    for key, value in item.items():
        if key == sys.argv[2]:
            print(value)
