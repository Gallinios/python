at=arithmoi = []

for i in range(10):
    num = float(input(f"eisagete toon arithmo {i+1}: "))
    arithmoi.append(num)
count = 0
total_sum = 0
for num in arithmoi:
    if num > 10:
        count += 1
        total_sum += num

print(f"arithmos megaliteros apo to 10: {count}")
print(f"athrisma megalytero apo to 10: {total_sum}")
