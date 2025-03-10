
altura = float(input("Qual o seu peso: "))
sexo = input("Qual seu sexo: ").upper()



match sexo:
 case "M": 
  peso_ideal = (72.7 * altura) - 58
 case "F": 
  peso_ideal = (62.1 * altura) - 44.7
 case _:
   print("opção invalida")
 

print(f"peso ideal {peso_ideal}.")

