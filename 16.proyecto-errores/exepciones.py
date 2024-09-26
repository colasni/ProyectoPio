try: 
    numero_1 = int(input("ingresa el numero 1: "))
    numero_2 = int(input("ingresa el numero 2: "))

    suma1y2 = numero_1 + numero_2
    
    print(suma1y2)
    
except ValueError:
    print("Dato ingresado no valido")