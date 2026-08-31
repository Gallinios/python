sum=0
mathimata=int ( input("mathimata:"))
for i in range(mathimata):
    vathmos = float (input("dose vathmo:"))
    sum=sum+vathmos
mo=sum/mathimata
print("m.o=",mo)
if(mo>=10):
    print("proagetai")
else:
    print("den proagetai")
