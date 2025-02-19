"""
Elabore um algoritmo para solicitar ao  usuario um valor e escrever a mensagem: E MAIOR  QUE 10!

Se o valor lido for maior que 10, caso contrário escrever: 
NÃO E MAIOR  QUE 10!


"""
import os 
os.system("clear")

valor_usuario =  int(input("Escreva um numero: "))

if valor_usuario > 10:
    print("E MAIOR QUE 10! ")
else:
    print("NÃO E MAIOR QUE 10 !")

