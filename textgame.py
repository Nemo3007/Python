#příliš mnoho možností a příliš málo času. S tímto by se dalo tvořit dalších deset hodin.
print("Vítej v této prazvláštní textové hře. ")
jmeno=input("Jak se zde budeš nazývat? ")
print(f"Tak jo {jmeno} je čas začít.")
print("Nacházíš se v temném lese a nemáš ponětí kam se vydat. Naštěstí máš u sebe pár opravdu užitečných věcí, hodinky, lovecký nůž, bezedný batoh a dalekohled. ")
print("Máš pár možností: ")
print("1. Zkusit vylézt na strom.")
print("2. Vydat se z kopce dolů.")
print("3. Vydat se do kopce")
gm1=True

while gm1:    
    v1=input("Jakou volbu zvolíš?")      
    if v1=="1"    
        gm2=True
        while gm2:
            print("Asi deset metrů od tebe vidíš strom, který je vhodný na rozhlídnutí se.")
            print("Když dolezeš na první větev stromu, uslišíš volání o pomoc.")
            print("Co uděláš?")  
            print("1. Vydáš se za voláním")      
            print("2. Počkáš, zda se volání nepřiblíží")
            print("3. vylezeš výš")
            v2=input("Musíš se rozhodnout rychle. ")

            if v2=="1":
                print("Seskočíš ze stromu a běžíš směrem k volání, které se približuje nebezpečně rychle. ")                
                print("V tom se před tebou objeví trpaslík s Medvědem v závěsu.")
                print("Bohužel ti trpaslík proběhne pod nohami a zároveň tě podrazí. Jen za sebou zařve: Moc se vám omlouvám. a běží dál.")
                print("GAME OVER")
                input("Pro ukončení zadej 1 pro vrácení se na začátek")
                exit()

            elif v2=="2":
                print("Čekáš na své větvi pln obav co se stane dál,když si všimneš trpaslíka pronásledovaného medvědem.")
                print("Trpaslík si tě všimne taky, a zamíří k tobě.")
                print("Jenže mu musíš pomoct se dostat na strom, trpaslík je příliš malý. ")
                print("1. Můžeš mu podat ruku a vytáhnout ho na větev. Zároveň musíte vylézt z dosahu medvěda. ")
                print("2. Vyprdneš se na Trpaslíka.")
                v3=input("Teď už určitě víš jak to funguje.  ")
                gm2=False
                while :
                    if v3=="1":
                    print("Zvládl jsi zachránit trpaslíka, a ani jsi nespadl ze stromu.")
                    print("Po dlouhé rozmluvě s trpaslíkem se od něho dozvíš kudy se dostaneš z lesa. Mezitím si medvěd nechal přejí chuť.")
                    print("You win")
                    elif v3 =="2":
                        print("Nechal jsi trpaslíka napospas medvědovi.")
                        print("Alespoň si tě medvěd nevšímá, takže se můžeš odpížit. ")
                        print("Medvědovi jsi sice unikl, ale pořád nemáš ponětí kam se vydat.")
                        print("Lesem bloudíš celé dny, a pořád se ti nedaří se z lesa dostat. Už by jsi si rád odpočinul.")
                        print("Hlava ti padá únavou. Už nemůžeš dál. Z vyčerpání padáš k zemi.")
                        print("GAME OVER")
                       
                    else:
                        print("Jsi fakt pěkný manták. To ti ještě nedošlo že musíš zadávat čísla?!")
            elif v2=="3":
                print("V klidu dál lezeš na strom, když si všimneš postavy co utíká před obrovským medvědem.")
                print("Bohužel jsi strašný nešika a s neúplným soustředěním ti lezení po stromech nejde.")
                print("Ležíš na zemi v kaluži krve. GAME OVER")
                gm2=False
            else:
                v2=input("Nějak ti to rozhodování nejde.")
    elif v1=="2":
        print(" ")
    elif v1=="3":
            v4=input("Dorazil jsi k obrovskému útesu s jeskyní.Prozkoumáš ji 1 nebo půjdeš dál podle útesu? 2 ")
            if v4 =="1":
                print("")
            elif v4 =="2":
                print("")
            else:
                    print("Jsi ")
    else:
        print("Musíš se rozhodnout...")
print("konečně jsi to zvládl se dostat k opravdovému konci. Evolvnul jsi se na boha")
