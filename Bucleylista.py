contador = 0 
i = 1
while i <= 10:
    if i % 2 == 0:
        contador += 1
    i += 1
print(f"pares: {contador}")
# Resultado: pares 5


suma = 0 
i = 1
while i  <= 100:
    suma += i
    i += 1
print(f"total: {suma}")
#Resultado Total: 5050
  
import random
numero_seceto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("adivina (1-100): "))
    intentos += 1
    if intento < numero_seceto:
        print(f"Mas alto ")
        
    elif intento > numero_seceto:
        print("Mas bajo.")
    
    elif intento > 7:
        print("intentos limites.")
    
    else:
        print(f"Correcto en "
              f"{intentos} intentos.")
        break