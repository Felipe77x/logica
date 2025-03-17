import os
os.system("cls || clear")


soma = 0 
nota = 0
media = 0
for i in range(3):
 nota =  float(input("Digite suas notas:"))
 soma += nota

 media = soma / 3
if media >= 7:
  print("Aluno aprovado.")
elif  media <= 4: 
  print("Aluno reprovado.")
else:
  print("Recuperação")