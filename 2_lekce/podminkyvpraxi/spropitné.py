
u=int(input("Účet v kč: "))
s=int(input("Spropitné v procentech: "))/100
p=int(input("Počet osob: "))
sp=(u*s)
print(f"Spropitné: {sp}")
cu=(u+sp)
print(f"Účet se spropitným: {u+sp}")
print(f"Cena na osobu: {cu/p}")
while True:
    volba=input("Chcete zadat další účet? ")
    if volba=="ne":
        exit()
    elif volba=="ano":
        break
    else:
        print("Zadejte správnou volbu.")

