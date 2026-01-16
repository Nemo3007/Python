i=1
while i <=10:
    print("Ahoj")
    i +=1
o=10
while o >0:
    print(o)
    o-=1
print("start")
heslo=("Dvorak")
hesloin=input(" Zadejte heslo: ")
while hesloin != heslo:

    hesloin=input(" Zadali jste nesprávné  heslo. Zkuste to znovu: ")
print("správně")
#menu aplikace
print(" Vítejte v aplikaci")
while True:
    print("======MENU======")
    print("1) začátek hry ")
    print("2) ukončení hry")
    volba=input("")
    if volba == "1":
        while True:    
            print("První lokace hry")
            volba2=input("Pro ukončení hry zadejte 1: ")
            exit()
    elif volba== "2":
        exit()
