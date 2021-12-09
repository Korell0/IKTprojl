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
    leggyakoribb = {}
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
                    top_3 = gyakori_szamok[:3]
        for i in num_counter.items():
            if i[0] in top_3:
                leggyakoribb[i[0]]=i[1]
        return leggyakoribb
                


                




