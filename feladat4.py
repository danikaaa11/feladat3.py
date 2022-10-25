import random

print("Ebben a játékban az a lényeg hogy eltalálja hogy fej vagy írás")
print("A tippnél adja meg hogy fej vagy írás")

user=int(input("Adja meg hogy fej vagy irás: "))

fej=1
iras=2

pc=random.randint(1,2)
user=random.randint(1,2)

if(pc>user):
    print("a játékos vesztett")   
else:
    print("a játékos nyert")
    









