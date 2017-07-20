from goodtables import validate
import csv
file = open('MOCK_DATA.csv', 'r')
reader = csv.reader(file)
for line in reader:
    print line
print(validate(file))
