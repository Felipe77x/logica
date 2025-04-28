
import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass


class Endereco:
    logradouro: str
    numero:str




class Pessoa:
    nome:str
    idade:int
    endereco: Endereco
   


    def exibir_dados(self):
        print(f"Nome: {self.nome} idade: {self.idade} Logradouro: \
            {self.endereco.logradouro} Numero: { self.endereco.numero}")
        



Endereco1 = Endereco("Rua A", "33")
Pessoa1 = Pessoa("Marta", 22, Endereco1)


print("Dados da pessoa")
Pessoa1.exibir_dados()