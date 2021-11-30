import csv
 
with open('otos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        nyeroszamok = row[4]


        