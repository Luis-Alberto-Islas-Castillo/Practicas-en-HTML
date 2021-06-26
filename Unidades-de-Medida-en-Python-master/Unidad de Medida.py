a=int(raw_input("Ingresa los litros de agua dedicadas ala casa: "))
b=a*0.001
x=a*0.0353 
print ("son"),b,("metros cubicos")
print ("son"),x,("pies cubicos")

c=int(raw_input("Ingresa los litros de agua dedicada al riego: "))
d=c*0.001
y=c*0.0353 
print ("son"),c,("metros cubicos")
print ("son"),y,("pies cubicos")

e=b+d*0.001
w=x+y*0.001
print("el total de litros es: "),e
print("el total de litros en pies cubicos es"),w
