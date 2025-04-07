
def inteiro_ou_negativo(numero):
    if numero == 0:
        print(f"O numero {numero} é neutro.")
    elif numero > 0:
        print(f"O numero {numero} é positivo.")
    elif numero < 0:
        print(f"O numero {numero} é negativo.")
numero = int(input("Digite um numero:"))

print(inteiro_ou_negativo(numero))