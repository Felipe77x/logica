

import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class usuarios:
    nome: str
    data_nascimento: int
    rg: int
    cpf: int

    def exibit_dados(self):
             print(f"Nome: {self.nome} \n data_nascimento: {self.data_nascimento} \n {self.rg} \n {self.cpf} \n \n")

quantidade = 1
lista_usuario = []
for i in range(quantidade):

        usuario = usuarios (
            nome = input("Digite o nome do usuario:"),
            data_nascimento = input("Digite a data de nascimento do usuario:"),
            rg = input("Digite o rg do usuario:"),
            cpf = int(input("Digite o cpf do usuario: "))
        )


   




        lista_usuario.append(usuario)


        nome_arquivo = "escravidão@ifood.txt"
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            for usuario in lista_usuario:
                arquivo.write(f"{usuario.nome}, {usuario.data_nascimento}, {usuario.rg} {usuario.cpf} \n")

        print("\nLivros salvos com sucesso no arquivo 'escravidão@ifood.txt'.")


