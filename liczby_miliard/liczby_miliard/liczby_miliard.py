import kod1
import kod2


liczby=[]
f=open("c:\\Temp\\liczby.txt","r")
for x in f:
    liczby.append(x)
f.close()

print(liczby)


evenList = []
for x in liczby:
   if int(x) % 2 == 0:
      evenList.append(x)
print(evenList)
print("liczba liczb parzystych w pliku: ", len(evenList))

tabSum =[]
for x in liczby:
    tabSum.append(kod1.getSum(int(x)))

print(tabSum)

f=open("c:\\Temp\\lcz1.txt","w")

f.writelines(str(tabSum))
f.close()



i=max(tabSum);
indi = tabSum.index(i)

j=min(tabSum);
indj = tabSum.index(j)

print("element o największej sumie: ", "index:",max(tabSum),"wartość: ", liczby[indi]);
print("element o największej sumie: ", "index:",min(tabSum),"wartość: ", liczby[indj]);

#liczby z cyframi rosnącymi

rosnace =[]
for x in liczby:
    if kod2.isCorrectOrder(int(x)) == True:
        rosnace.append(x)
        
f=open("c:\\Temp\\lcz2.txt","w")

f.writelines(str(rosnace))
f.close()

print(rosnace)


#liczby z cyframi rosnącymi występujące w kolejności bezpośrednio po sobie

kolejne =[]
for x in liczby:
    if kod2.check(int(x)) == True:
        kolejne.append(x)
        
f=open("c:\\Temp\\lcz3.txt","w")

f.writelines(str(kolejne))
f.close()

print(kolejne)


