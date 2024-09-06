# toets 1 - 6

from time import sleep


oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))


for _ in range(3):
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)


prijs_m2 = 40  
if oppervlakte >= 150:
    prijs_m2 = 35
elif oppervlakte >= 80:
    prijs_m2 = 38

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag voor een oppervlakte van {oppervlakte} m2 is: Eur {totaal}')