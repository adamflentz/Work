from goodtables import validate
import collections
import json
validator = validate('MOCK_DATA.csv', error_limit=1000000, row_limit=1000000, schema='schema.json', order_fields=True)
errorlist = []
print (validator)
for element in validator['tables'][0]['errors']:
    print(element['message'])

