def nota(primeira_nota, segunda_nota):
    media = (primeira_nota + segunda_nota) / 2
    if media >= 7:
        print("Aprovado")
    else:
        print("Aprovado")
    return media
primeira_nota = int(input("Digite sua primeira nota:"))
segunda_nota = int(input("Digite sua segunda nota:"))

media = nota(primeira_nota, segunda_nota)
print(media)



