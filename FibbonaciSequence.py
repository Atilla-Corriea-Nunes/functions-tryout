nterms = int(input("Hoe veel termen? "))

def fibbonaci(n1, n2, count, nterms):  
    if nterms <= 0:
       print("Vul aub een positief cijfer in")

    elif nterms == 1:
       print("Fibonacci reeks tot",nterms,":")
       print(n1)

    else:
       print("Fibonacci Reeks:")
       while count < nterms:
            print(n1)
            if count + 1 < nterms:
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
            else:
               break
    print("")
    return "De gulden snede is dus "+ str(n1)

print(fibbonaci(0, 1, 0 ,nterms))
