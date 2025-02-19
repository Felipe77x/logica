

numero1 = int(input("Digite o numero:"))
numero2 = int(input("Digite o numero:"))


media = (numero1 + numero2) / 2
soma = numero1 + numero2
produto = numero1 * numero2

if numero1 < numero2:

 menor = numero1
 maior = numero2

else:
  menor = numero2
  maior = numero1

print(f"\n Exibindo resultados:")

print(f"Media:{media}")
print(f"Soma:{soma}")
print(f"Produto:{produto}")
print(f"Maior:{maior}")
print(f"Menor:{menor}")
