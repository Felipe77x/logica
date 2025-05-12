import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass

class usuario:
    nome: str
    data_nascimento: int
    ra: int
    curso:str
    endereco: str


class endereco:
    logradouro: str
    numero: int
    cidade: str
    estado:str


list_alunos = [ ] 

def inserir_funcionario(list_alunos):
    
    alunoss = usuario (nome = input("Digite seu nome :"),
    data_nascimento = int(input("Digite seu nome :")),
    ra = int(input("Digite seu nome :")),
    curso = input("Digite seu nome :"),
    endereco = input("Digite seu nome :")
    )
    list_alunos.append(alunoss)
    print(list_alunos)

