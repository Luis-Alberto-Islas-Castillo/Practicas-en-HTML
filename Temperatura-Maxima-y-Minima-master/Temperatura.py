a=[]
cont=0
min_temp = 100000
max_temp = 0
b=input("Ingresa el numero de cantidades")
for z in range(b):
    
    a.append(input("Ingresa la temperatura"))
    cont=cont+a[z]+0.0
    promedio=cont/10.0

    cont = cont+a[z]
    if a[z]<min_temp:
        min_temp = a[z]
    if a[z]>max_temp:
        max_temp = a[z]

    
print("Temperatura"),a
print cont
print("Promedio de temperaturas:"),promedio
print("La temperatura minima es:"),min_temp
print("La temperatura maxima es:"),max_temp
