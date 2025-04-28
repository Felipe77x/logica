import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass

class pessoa:
    nome: str
    idade: int


@dataclass

class pet:
    nome: str
    idade: int
    raca: str

#atribuindo valores


pessoa1 = pessoa("Marta", 30)
pessoa2 = pessoa("Felipe Dias", 20)


print(f"Nome: {pessoa1.nome}     Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}     Idade: {pessoa2.idade}")

