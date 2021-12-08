import csv


def nyeroszamok():
    
    with open('otos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            nyeroszamok = row[4]
            ered = nyeroszamok.split(";")
            del ered[0]
            new_list = []
            ered = [int(i) for i in ered]
            new_list.append(sum(ered))
            print(new_list)
def legkisebb():
    with open('otos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            nyeroszamok = row[4]
            ered = nyeroszamok.split(";")
            del ered[0]
            ered = [int(i) for i in ered]
            newlist = []
            newlist.append(ered)
            print(newlist)
            
nyeroszamok()

