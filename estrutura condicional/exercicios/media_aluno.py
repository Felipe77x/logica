

import os
os.system("clear")

nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7: 
   print(f"Aluno aprovado  {media}")
elif media < 7:
   print(f"O aluno ficou de recuperação com a {media}")
else:
   print(" O aluno foi reprovado por falta" )


