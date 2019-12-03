import webbrowser as wb
from math import factorial

def menu():
    print("Selecciona la distrivucion que quiera usar.")
    print("1. Normal ")
    print("2. Binomial ")
    print("3. Hipergeometrica")
    print("4. Salir")

def normal():
    print("Espera un momento.........Listo")
    valor = float(input("Dato a calcular: "))
    media = float(input("Ingresa la media: "))
    desviacion = float(input("Ingresa la desviacion tpica: "))
    resultado=(valor-media)/(desviacion)
    print("La cantidad que debes buscar en la tabla de distribucion es: ", resultado)
    segundo_valor = float(input("Segundo Dato a calcular: "))
    segundo_resultado=(segundo_valor-media)/(desviacion)
    print("La cantidad que debes buscar en la tabla de distribucion es: ", segundo_resultado)
    primer_resultado = float(input("Equivalencia del primer resultado: "))
    segundo_resultado = float(input("Equivalencia del segundo resultado: "))
    final=primer_resultado-segundo_resultado
    print("La distibucion Normal es " , final)

def binomial():
    muestra = float(input("Ingresa el total de muestra: "))
    n_exitos = float(input("Ingresa el numero de  exitos: "))
    p_exito = float(input("Ingresa el la probabilidad de exito: "))
    fracasos = float(input("Ingresa la probabilidad de fracaso: "))
    resultado=factorial(muestra)
    resultado_dos=factorial(n_exitos)
    prueba=pow(p_exito,n_exitos)
    prueba_dos=pow(fracasos,muestra-n_exitos)
    print ("El resultado es ",resultado/resultado_dos*prueba*prueba_dos)
    print ("El resultado convertido en porcentage es ",resultado/resultado_dos*prueba*prueba_dos*100,"%")

def hipergeometrica():
    elementos_entrada = int(input("Ingresa el total de elementos de entrada: "))
    numero_elementos = int(input("Ingresa el número de elentos: "))
    probabilida_exito = int(input("Ingresa las probabilidades de éxito: "))
    probabilida_fracaso = int(input("Ingresa las probabilidades de fracaso: "))
    reul_hiper=(elementos_entrada-numero_elementos*probabilida_exito)/((numero_elementos*probabilida_exito*probabilida_fracaso)**1/2)
    print(reul_hiper)

def tabla():
    wb.open_new(r'D:\estadistica\PDF\Distribucion_Normal.pdf')


while True:    
    menu()
    distribucion= input("Selecciona el numero correspondiente para cada distribucion: ")

    if distribucion=="1":
        tabla() 
        normal() 
        input("\npulsa una tecla para regresar al menu: ")
    elif distribucion=="2":
        binomial()
        input("\npulsa una tecla para regresar al menu: ")
    elif distribucion=="3":
        hipergeometrica()
        input("\npulsa una tecla para regresar al menu: ")
    elif distribucion=="4":
        break
    else:
        input("El numero que pulsaste no corresponde a ninguna distribucion.\npulsa una tecla para regresar al menu: ")
