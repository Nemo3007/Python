#for cyklus
for cislo in range(5):
    print (f"{cislo}")
#pole
zelenina=["mrkev","brambora","rajče"]
print(zelenina)
print(zelenina[0])
for k in zelenina:
    print(f"Miluju: {k}")
#N-tice v poli
otazky=[("Kolik je 4*4?","16"),("kolik je 56-69?","13")]
body=0
otazky=0
for ot,od in otazky:
    odpo=input(f"{ot}")
    
    if odpo == od:
        print("správně")
        body+=1
    else:
        print("špatně")
        otazky+=1
input(f"Dokončil jis můj test. Dosáhl jsi {body} bodů z {otazky}")

