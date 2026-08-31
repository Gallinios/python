#sc = int(input("Δώσε έναν αριθμό: "))
#guess = int(input("Μαντεψε τον αριθμο"))
#while sc!=guess:
#        guess=int(input("ξανα μαντεψε τον αριθμο:"))
#print(f"Το {guess} ηταν ο μυστικος αριθμος")


#sc = int(input("Δώσε έναν αριθμό: "))
#guess = int(input("Μαντεψε τον αριθμο"))
#for i in range(2):
#    if sc!=guess:
#        guess=int(input("ξανα μαντεψε τον αριθμο:"))
#    else:
#        print(f"Το {guess} ηταν ο μυστικος αριθμος")
#        break


sc = int(input("Δώσε έναν αριθμό: "))
guess = int(input("Μαντεψε τον αριθμο"))
for i in range(2):
    if sc!=guess:
        guess=int(input("ξανα μαντεψε τον αριθμο:"))
        if sc>guess:
            print("Ο αριθμος που ψαχνεις ειναι μεγαλυτερος απο τον {guess}")
        else:
            print("Ο αροθμος που ψαχνεις ειναι μικροτερος απο το {guess}")
    else:
        print(f"Το {guess} ηταν ο μυστικος αριθμος")
        break





