import random
import mujmodul

cislo=random.randint(1,10)
print(cislo)

print(mujmodul.mojecislo)

c2=random.randint(1,6)
print(f"Hodil jsi {c2}")

ovoce = ["banán","jablko","rajče"]
ovoce[2]="pomeranč"
ovoce.append("mandarinka")
print(ovoce[0])
print(ovoce[-1])
print(ovoce[1])
print(random.choice(ovoce))

kamarádi=["Jarda", "Tomáš", "Vojta", "Radek"]
print(f"{random.choice(kamarádi)} musí zaplatit účet.")



ovoce1=["jahody", "nektarinky"]
zelenina=["kedlubna", "brambora"]
vnoreny_seznam=[ovoce,zelenina]
print(vnoreny_seznam[0][0])
