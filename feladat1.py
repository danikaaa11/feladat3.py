import math

x1 = float(input("Adja meg, hogy hol helyezkedik el az első pont az x tengelyen: "))
y1 = float(input("Adja meg, hogy hol helyezkedik el az első pont az y tengelyen: "))
xketto = float(input("Adja meg, hogy hol helyezkedik el a második pont az x tengelyen: "))
yketto = float(input("Adja meg, hogy hol helyezkedik el a második pont az y tengelyen: "))

c_negyzetx = math.pow(xketto - x1,2)
c_negyzety = math.pow(yketto - y1,2)
c_osszeg = c_negyzetx + c_negyzety
vegeredmeny = math.sqrt(c_osszeg)

print(vegeredmeny)