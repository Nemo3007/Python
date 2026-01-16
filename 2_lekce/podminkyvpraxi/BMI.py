m=int(input("Zadejte hmotnost osoby v kg: "))
h=int(input("Zadejte výšku osoby v cm: "))
h2=(h/100)
bmi=(m/(h2**2))
print(f"{bmi:.1f}")
if bmi < 18.5:
    print("Podváha")
elif 18.5<=bmi<=24.9:
    print("Normální váha")
elif 25<=bmi<=29.9:
    print("Nadváha")
elif 30<=bmi<=34.9:
    print("Obezita I. stupně")
elif 35<=bmi<=39.9:
    print("Obezita II. stupně")
else:
    print("Obvezita III. stupně")