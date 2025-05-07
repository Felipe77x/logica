import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: int



    def exibir_detalhes(self):
        print(f"Titulo: {self.nome}\n Ano: {self.data_admissao} \n Autor: {self.matricula} \n endereco: {self.endereco} \n ")

@dataclass
class cliente:
    nome: str
    data_nascimento: int
    endereco: int
    
    def exibir_detalhes(self):
        print(f"Titulo: {self.nome}\n Ano: {self.data_nascimento} \n  {self.endereco} \n ")


quantidade = 1
quantidades = 1
lista_funcionario = []
lista_cliente = []

for i in range(quantidade):
    funcionario1 = funcionario (
        nome = input("Digite seu nome:"),
        data_admissao = int(input("Digite a data de admissão:")),
        matricula = int(input("Digite sua matricula:")),
        endereco = input("Digite seu endereco:")
    )

    lista_funcionario.append(funcionario1)

for ok in range(quantidades):
    cliente1 = cliente (
        nome = input("Digite seu nome:"),
        data_nascimento = int(input("Digite a data de admissão:")),
        endereco = input("Digite seu endereco:")
    )

    lista_cliente.append(cliente1)


funcionario_empresa = "funcionarios_senai.txt"
with open(funcionario_empresa, "a", encoding="utf-8") as arquivo:
    for funcionario1 in lista_funcionario:
        arquivo.write(f"{funcionario1.nome}, {funcionario1.data_admissao}, {funcionario1.matricula}, {funcionario1.endereco}\n")

cliente_empresa = "cliente_senai.txt"
with open(cliente_empresa, "a", encoding="utf-8") as arquivo:
    for cliente1 in lista_cliente:
        arquivo.write(f"{cliente1.nome}, {cliente1.data_nascimento},  {cliente1.endereco}\n")

print("\nLivros salvos com sucesso no arquivo 'livraria.txt'.")

