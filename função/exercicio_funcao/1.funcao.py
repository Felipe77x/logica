"""
faça uma função sem retorno com o nome: logo_senai()
Limpando o terminal e inserindo: === SENAI DENDEZEIROS
Solicite ao usuario dois números
cada um em uma variável diferente
Crie uma função com retorno para somar os números informados pelo usuario
"""

def logo_senai():
    import os
    print("=== SENAI DENDEZEIROS ===")
numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite um numero:"))

def soma():
    somas = numero1 + numero2
    return somas

print(soma())