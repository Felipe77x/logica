lista_notas = []

for i in range(3):
    nota = float(input("Digite suas notas:"))
    lista_notas.append(nota)
    soma = sum(lista_notas) 
    media = soma  / 3

for nota in lista_notas:
    print(f"O valor da média é {media:.2f}.")
