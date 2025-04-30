import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class funcionario:
    nome: str
    data_nascimento: str
    rg: int
    cpf: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.data_nascimento} \npeso:{self.rg} \naltura: {self.cpf} \n \n")

quantidade_vezes = 1
lista_funcionario = []


for i in range(quantidade_vezes):
    funcionario1 = funcionario(
        nome = input("Digite sua nome:"),
        data_nascimento = input("Digite sua data de nascimento:"),
        rg = int(input("Digite seu rg:")),
        cpf = int(input("Digite seu cpf:"))
    )

    lista_funcionario.append(funcionario1)


livros = "funcionario.txt"
with open (livros, "a") as livros:
    for livro1 in lista_funcionario:
        livros.write(f"{funcionario1.nome}, {funcionario1.data_nascimento}, {funcionario1.rg}, {funcionario1.cpf}")