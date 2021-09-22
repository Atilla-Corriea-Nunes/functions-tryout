
cinput = int(input("Van welk cijfer wilt u de tafel zien? (1 tot 10) "))



def tafel(cijfer):
    print ("De tafel van "+ str(cijfer))
    
    for teller in range(1,11):
       print(teller ," x ", cijfer ," = ", teller * cijfer)

tafel(cinput)