


#Desenvolva um programa que receba como entrada um numero inteiro que represente um dos 7 dias da semana
#e imprima na tela se esse dia e util, final de semana ou invalido.
#Considere que Domingo e o  dia  1 e Sabado o dia 7.



dir = int(input("Digite um numero"))

match dir:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda dia e útil.")
  case 3:
    print("Terça dia e útil.")
  case 4:
    print("Quarta dia e útil.")
  case 5:
    print("Quinta dia e útil.")
  case 6:
    print("Sexta dia e útil.")
  case 7:
    print("Sábado")
  case _:
    print("Inválido")

print(dir)