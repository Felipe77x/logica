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

quantidade_vezes = 4
lista_paciente = []

for i in range(quantidade_vezes):
    pessoa1 = pessoa(
        nome = input("Digite sua nome:"),
        idade = int(input("Digite sua idade:")),
        peso = float(input("Digite sua peso:")),
        altura = float(input("Digite sua altura:"))
    )

    lista_paciente.append(pessoa1)


for pessoa1 in lista_paciente:
    pessoa1.exibir_dados()
