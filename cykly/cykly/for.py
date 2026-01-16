x=input("kolik je 2+2?")
pb=0
if x=="4":
    print ("správně")
    pb+=1
else:
    print("špatně")
x2=input("Jaké je hlavní město Německa? ")
if x2=="Berlín":
    print("správně")
    pb+=1
else:
    print ("špatně")
print(f"Konec testu, dosahl jsi {pb} bodů")