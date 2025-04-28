import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass

class login:
    nome: str
    email: str
    telefone: int
    endereco: str


login_pessoa = login("Felipe Dias", "Dias80@Alenda", 71900099, "Rua python")

print(f"Nome: {login_pessoa.nome} Email: {login_pessoa.email} Telefone: {login_pessoa.telefone} Rua: {login_pessoa.endereco}")