nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
    print("Aprovado")
elif media >= 7.5:
    conceito = "B"
    print("Aprovado")
elif media >= 6:
    conceito = "C"
    print("Aprovado")
elif media >= 4:
    conceito = "D"
    print("Reprovado")
else:
    conceito = "E"
    print("Reprovado")

print(f"Meu nome é {nome}, minhas duas notas foram {nota1} e {nota2}, e minha média foi {media:.2f} com conceito {conceito}.")