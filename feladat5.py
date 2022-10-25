import random

#lista = int(input("Adja meg, hogy hány elemű listát szeretne: "))
hossz = int(input("Adja meg a hosszt: "))

for i in range(hossz):
    alista = [*range(-100, 100+1)]
    veletlen = random.choice(alista)
    print(veletlen)
