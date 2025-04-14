
lista_numero = []
for i in range(5):
    numeros = int(input("Digite seus numeros:"))
    lista_numero.append(numeros)
    numero_max = max(lista_numero)
    numero_min = min(lista_numero)

print(f"O numero maximo é {numero_max}")
print(f"O numero minimo é {numero_min}")
print(f"Os numeros informados pelo usuario foram {lista_numero}")


listas_numeros = []
quantidades_numeros = 5

print("= Solicitado números =")

for i in range(quantidades_numeros):
    numero = int(input(f"Digite o {i+1}º número:"))
    listas_numeros.append(numero)

maior = max(listas_numeros)
menot = min(listas_numeros)

print("\n Mostrando numero")