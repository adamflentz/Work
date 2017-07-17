import sys, csv


reader = csv.reader(open("MOCK_DATA.csv"))
tempCSV = [l for l in reader]
for row in tempCSV:
    count = 0
    for x in row:
        if x == "":
            findElement = row.index(x)
            row[count] = "empty"
        count += 1
print(tempCSV)
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(tempCSV)

