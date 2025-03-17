
pares = 0 
impares = 0


 
for i in range(5):

 impares_pares = int(input("Digite um numero:"))

if impares_pares % 2 == 0:
  pares += 1
else: 
 
  impares += 1

print(f"pares: {pares}")
print(f"impares {impares}")
print("\n FIM PROGRAMA")