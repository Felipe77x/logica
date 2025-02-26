"""
Faça um algoritmo que solicite ao usuario dois numeros 
e um caractere 


"""

primeiro_numero = int(input("Digite um numero:"))
operador = (input("Digite a operação que deseja (+ - * /):"))
segundo_numero = int(input("Digite um numero:"))


#Processamento 

match operador:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero - segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero

# Saida

print(f"\n Primeiro número: {primeiro_numero}")
print(f"Operação {operador}")
print(f"Segundo numerro {segundo_numero}")
print(f"Resultado {resultado}")

