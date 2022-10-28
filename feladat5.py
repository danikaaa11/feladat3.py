import random

#lista = int(input("Adja meg, hogy hány elemű listát szeretne: "))
'''hossz = int(input("Adja meg a hosszt: "))

for i in range(hossz):
    alista = [*range(-100, 100+1)]
    veletlen = random.choice(alista)
    print(veletlen)'''
    
N=int(input("Hány elemmel  akarsz dolgozni: "))    
 
Lszamok=[]    
    
for i in range(N): #N=3 0,1,2
    Lszamok.append(random.randint(-100,100))
    
print(Lszamok)

#a
negativdb=0
for szam in Lszamok:
    if(szam<0):
        negativdb+=1 #negativdb=negativdb+1

print("Negatív számok száma: ",negativdb)

#b rész
print(max(Lszamok)-min(Lszamok))
print()



           