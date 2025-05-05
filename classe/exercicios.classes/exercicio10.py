import os
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Autor:
    nome: str
   
    biografia: str
    

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f"Titulo: {self.titulo}\n Ano: {self.ano} \n Autor: {self.autor.nome} ")

quantidade_vezes = 1
lista_livro = []


for i in range(quantidade_vezes):

    livros = Livro(
        titulo = input("Digite o titulo livro"),
        ano = int(input("Ano publicação")),
        autor = Autor(
                nome = input("Digite titulo do livro"),
                biografia = input("Digite titulo do livro")
    ))

    lista_livro.append(livros)


nome_arquivo = "livraria.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    for livro in lista_livro:
        arquivo.write(f"{livro.titulo}, {livro.ano}, {livro.autor.nome}\n")

print("\nLivros salvos com sucesso no arquivo 'livraria.txt'.")



