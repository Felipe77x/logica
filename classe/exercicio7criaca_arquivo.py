import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \npeso:{self.peso} \naltura: {self.altura} \n \n")

quantidade_vezes = 1
lista_paciente = []

for i in range(quantidade_vezes):
    pessoa1 = pessoa(
        nome = input("Digite sua nome:"),
        idade = int(input("Digite sua idade:")),
        peso = float(input("Digite sua peso:")),
        altura = float(input("Digite sua altura:"))
    )

    lista_paciente.append(pessoa1)


nome_arquivo = "Dados das pessoas.txt"
with open(nome_arquivo, "a") as nome_arquivo:
    for pessoa1 in lista_paciente:
        nome_arquivo.write(f"{pessoa1.nome}, {pessoa1.idade}, {pessoa1.peso}, {pessoa1.altura}")


for pessoa1 in lista_paciente:
    pessoa1.exibir_dados()
