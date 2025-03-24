quantidades_nota = 3
soma = 0
for i in range(quantidades_nota):
    while True:
        nota = float(input("Digite suas notas"))
        if nota < 0 and nota > 10:
           print("A nota não pode ser menor que 0 e maior que 10.")
        else:
          soma += nota
          break
    
        media = (soma + quantidades_nota) / 3
              

        if media >= 7:
             print("Aprovado")
        elif media >= 5 and media >= 6.9:
             print("Recuperação")
        else:
             print("Reprovado")
            
             print(f"A média do aluno é {media}")