
import os
from  dataclasses import dataclass

os.system("cls || clear")

@dataclass

class arvore:
    nome: str
    idade: int
    peso: float
    altura: float


arvores = arvore("Felipe Dias", 20, 80, 1.80)


print(f"As caracteristicas da árvore são Nome: {arvores.nome}, Idade: {arvores.idade}, Peso: {arvores.peso}, Altura: {arvores.altura}")
