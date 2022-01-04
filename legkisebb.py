import csv

def legkisebbszam():
    with open('otos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        new_list = []
        kicsi = 500
        for row in spamreader:
            nyeroszamok = row[4]
            ered = nyeroszamok.split(";")
            del ered[0]
            ered = [int(i) for i in ered]
            new_list.append(sum(ered))
        for items in new_list:
            if items < kicsi:
                if items == 0:
                    continue
                else:
                    kicsi = items
        print(kicsi)

legkisebbszam()