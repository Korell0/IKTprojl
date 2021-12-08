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
        return kicsi

def leggyakoribbszamok():
    with open('otos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        new_list = []
        num_counter = {}
        for row in spamreader:
            nyeroszamok = row[4]
            ered = nyeroszamok.split(";")
            del ered[0]
            ered = [int(i) for i in ered]
            new_list.append(ered)
        for items in new_list:
            for numbers in items:
                if numbers > 99:
                    numbers = ""
                else:
                    if numbers in num_counter:
                        num_counter[numbers] += 1
                    else:
                         num_counter[numbers] = 1
                    gyakori_szamok = sorted(num_counter, key = num_counter.get, reverse = True)
                    gyakori_value = sorted(num_counter, value = num_counter.get, reverse = True)
                    top_3 = gyakori_szamok[:3]
                    top_value = gyakori_value[:3]
        print(top_3)
        print(top_value)
                
leggyakoribbszamok()



