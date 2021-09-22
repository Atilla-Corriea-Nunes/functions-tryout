while (True):
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    def deVraag(n, l):
        print("Hallo "+ n +", je leeftijd is ", l)
        print("")
    
    if (naam.lower() == "stop" or leeftijd.lower() == "stop"):
        quit()

    deVraag(naam, leeftijd)

    

