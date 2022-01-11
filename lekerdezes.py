import csv
from os import system

system('cls')

with open('D:\GitAdam\onelethtml\IKTprojl\otos.csv', 'r') as file:
    reader = csv.reader(file)
    tomb=[]
    line=0
    for row in reader:
        if  line==0:
            line=line+1
            continue
        else:
            line=line+1
            #print(row)
            line_tomb=[]
            line_tomb.append(row[0].split(';')[11:16])
            #print(line_tomb) 
            tomb.append(line_tomb)
    #teszteléshez
    #print(tomb[0])

#Beolvasás--------------------------
    sor_elso=[]
    sor_elso.append(tomb[0][0:5])
    print(sor_elso)
#Lekérdezés_1-----------------------
    sor_masodik=[]
    sor_masodik.append(tomb[1][0:5])
    print(sor_masodik)
#lekérdezés_2-----------------------
#    db=[]
#    print(len(tomb))
# #   for i in range(1,91):
 #   szamolo=0
#        for j in range(len(tomb)):
#            for n in range(5):
#                print(n)
#                if tomb[j][n] == i:
#                   szamolo+=1
#        db.append(szamolo)
  #  print(db)
  #  for i in range(len(db)):
 #       if db[i]==208:
 #           print(f"{i+1} 208")
 #       elif db[i]==209:
 #           print(f"{i+1} 209")
 #       elif db[i]==218:
 #           print(f"{i+1} 218")
#
    #sorba rendezés
    #sorrend=db
    #for i in range(len(sorrend)):
    #    for j in range(len(sorrend)-1):
    #        if sorrend[j]>sorrend[i]:
    #            c=sorrend[j]
    #            sorrend[j]=sorrend[i]
    #            sorrend[i]=c
    belso_tomb =[]
    final_tomb = []
    kicsi = 9999999999999999999
    for i in tomb:
        for l in i[0]:
            belso_tomb.append(int(l))
    for j in range(0, len(belso_tomb), 5):
        final_tomb.append(belso_tomb[j : j+5])
            
    for i in final_tomb:
        if sum(i) < kicsi:
            kicsi = sum(i)
            

    for i in final_tomb:
        if i[0]+1==i[1]:
            if i[1]+1==i[2]:
                if i[2]+1==i[3]:
                    print("ok3a")
                    if i[3]+1==i[4]:
                        continue
        elif i[1]+1==i[2]:
            if i[2]+1==i[3]:
                print("ok3b")
                print(i)
                if i[3]+1==i[4]:
                    print("ok4b")
        elif i[2]+1==i[3]:
                if i[3]+1==i[4]:
                    print("ok4c")  
                    print(i)      






