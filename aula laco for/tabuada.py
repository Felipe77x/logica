
print("Tabuada") 

numero_tabuada = int(input("Digite um numero:")) 
 
for numero_tabuada in range (1, 11):
 
 for tabuada in range(1, 11):
 
  resultado = numero_tabuada * tabuada



  print(f"{tabuada} X {numero_tabuada} = {resultado}")
  
""""
import os 
os.system("cls || clear")

numero = int(input("Digite um número para tabuada:"))
for i in range(1,11):
  print(f"{numero} X {i} = {numero * i }")

  print("FIM PROGRAMA")
  """