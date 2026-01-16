import random

nůžky ="nůžky"
papír="papír"
kámen="kámen"

game=[nůžky, papír, kámen]

vyhry=0
prohry=0
remízy=0

while True:
    pc = random.randint(0,2)
    print(f"Skóre: výhry {vyhry}, remízy {remízy} prohry {prohry}. ")
    uzivatel=int(input("0=nůžky, 1=papír, 2=kámen"))
    print(f"Pčítač dal {game[pc]}, ty jsi dal {game[uzivatel]} ")
    if (uzivatel==0 and pc==1) or (uzivatel==1 and pc==2) or (uzivatel==2 and pc==0):
        print("Výhra")
        vyhry+=1
    elif (uzivatel==0 and pc==0) or (uzivatel==1 and pc==1) or (uzivatel==2 and pc==2):
        print("remíza")
        remízy+=1
    else:
        print("prohra")
        prohry+=1