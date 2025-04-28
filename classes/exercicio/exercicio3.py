


import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass



class Peixe:
    nome: str
    peso: int
    sabor: str

    def peixes(self):
        print("\n Exibindo dados")
        print(f"Nome: {self.nome} peso: { self.peso}  sabor: {self.sabor}" )



nome = input("Digite o nome do peixe :")
peso = input("Digite o peso do peixe :")
sabor = input("Digite o sabor do peixe:")



peixe1 = Peixe(nome, peso, sabor)

# Chamando o método para exibir os dados
peixe1.peixes()



"""
import os
from dataclasses import dataclass

# Limpa o terminal
os.system("cls || clear")

@dataclass
class Peixe:
    nome: str
    peso: int
    sabor: str

    # Método para exibir os dados do peixe
    def peixes(self):
        print("\nExibindo dados")
        print(f"Nome: {self.nome} | Peso: {self.peso}g | Sabor: {self.sabor}")

# Entrada de dados
nome = input("Digite o nome do peixe: ")
peso = int(input("Digite o peso do peixe: "))  # Convertendo para inteiro
sabor = input("Digite o sabor do peixe: ")

# Criando objeto Peixe
peixe1 = Peixe(nome, peso, sabor)

# Chamando o método para exibir os dados
peixe1.peixes()

"""