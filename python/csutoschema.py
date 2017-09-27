import sys, json

schema_dict ={}
schema_fields = []

csvfile = open(sys.argv[1])
headerlist = csvfile.readline().split(', ')
for element in headerlist:
    field_dict = {}
    field_dict["name"] = element.strip()
    field_dict["title"] = element.strip()
    field_dict["type"] = "string"
    schema_fields.append(field_dict)
csvfile.close()
schema_dict["fields"] = schema_fields
valid_json = json.dumps(schema_dict)
sys.stdout.write(valid_json)

