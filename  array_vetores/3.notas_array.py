lista_notas = []
    
def calculo(media):   
    for i in range(4):
        nota = float(input("Digite suas notas:"))
        lista_notas.append(nota)
        soma = sum(nota)
        media = soma /4
        return media


def resultado(media):
    if media >= 7:
        print(f"O aluno foi aprovado com a nota {media:.2f}")
    elif media  <= 7:
         print(f"O aluno foi recuperação com a nota {media:.2f}")
    else:
         print(f"O aluno foi reprovado com a nota {media:.2f}")


    for nota in lista_notas:
     print(calculo())
     print(resultado())
     print(nota)
