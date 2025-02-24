numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite um numero:"))

maior = max( numero1, numero2)
menor = min( numero1, numero2)

if numero1 == numero2:
  print("Os numeros são iguais")



print(f"Primeiro numero:{numero1}")
print(f"segundo numero:{numero2}")
print(f"O maior numero {maior}.")
print(f"O menor numero {menor}.")