mathites = 10
vathmoi = 0
arista =poli_kala = kala = apotyxia = 0

for i in range(10):
    vathmos = float(input(f"Dose ton arithmo toy mathiti {i+1}:"))
    vathmoi = vathmoi + vathmos
    if vathmos >= 18:
        arista = arista + 1
    elif vathmos >=15:
        poli_kala = poli_kala +1
    else:
        apotyxia = apotyxia +1
        
print("Arista:",arista, "poli_kala:",poli_kala,"kala:",kala,"apotyxia:",apotyxia)
mesos_oros =  vathmoi /mathites
print("mesos oros taxis:", mesos_oros)
