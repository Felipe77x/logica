

import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class livro:
    nome: str
    autor: str
    categoria: str
    preco: float
    
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \npeso:{self.peso} \naltura: {self.altura} \n \n")


lista_livros = []
quantidades_vezes = 1

for i in range(quantidades_vezes):
    livro1 = livro(
        nome = input("Digite o nome do livro:"),
        autor = input("Digite o nome do livro:"),
        categoria = input("Digite o nome do livro:"),
        preco = int(input("Digite o nome do livro:"))
    )

    lista_livros.append(livro1)



livros = "Biblioteca de livros.txt"
with open (livros, "a") as livros:
    for livro1 in lista_livros:
        livros.write(f"{livro1.nome}, {livro1.autor}, {livro1.categoria}, {livro1.preco}")
