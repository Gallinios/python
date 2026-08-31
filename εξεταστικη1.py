grades = []

for i in range(10):
    while True:
        try:
            grade = float(input(f"arithmos fititi {i+1}: "))
            if 0 <= grade <= 10:
                grades.append(grade)
                break
            else:
                print("o vathmos prepei na einai 0 kai 10.")
        except ValueError:
            print("eisagetai enan ekeiro arithmo.")

perase = [g for g in grades if g >= 5]
apetixe = [g for g in grades if g < 5]

print(f"\n exoyne perasei: {len(perase)} mathites.")
print(f"kopikane: {len(apetixe)} mathites.")
print("oi mathites poy kopikane:", apetixe)
