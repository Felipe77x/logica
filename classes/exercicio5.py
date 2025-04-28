import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass

class usuario:
    nome: str
    email: str

@dataclass 

class endereco:

    logradouro: str
    numero: int
    cidade: str


    def exibir_dados(self, usuario):
        print("Exibir informação")
        print(f"Nome: {usuario.nome} Email: {usuario.email} Logradouro: {self.logradouro} Numero: {self.numero} Cidade: {self.cidade}")


nome = input("Digite seu nome:")
email = input("Digite seu email:")
logradouro = input("Digite seu logradouro:")
numero = input("Digite seu numero:")
cidade = input("Digite sua cidade:")

usuario1 = usuario( nome, email)
endereco1 = endereco(logradouro, numero, cidade)
endereco1.exibir_dados(usuario1)