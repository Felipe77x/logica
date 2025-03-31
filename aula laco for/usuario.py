
import os 
import time
os.system("cls || clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0

opcao = int(input("Digite a opção desejada: "))
match opcao:
    case 1:
        idade = int(input("digite sua idade:"))
        sexo = input("Informe seu sexo - Use 'M' ou 'F':").upper()
        salario = float(input("Digite seu salario:"))
        contador += 1
        soma_salario += salario
        maior_idade = max(maior_idade, idade)
        menor_idade = min(menor_idade, idade)

        if sexo == "F" and salario >= 5000:
            mulheres5k += 1
            os.system("cls || clear")
    case 2:
        if contador > 0:
         media_salario = soma_salario / contador
         print("\n Exibindo resultados = ")
         print(f"Média salarial do grupo:")
         print(f"Maior idade do grupo:")
         print(f"Menor idade do grupo")
         print(f"Quantidade de mulheres com salários a partir de 5k:")
        else:
           print("\n Não foram informados os dados necessários.")
           time.sleep(3)
           os.system("cls || clear")
    case 3:
        print("\n = FIM =")      
        break
    case _:
      print("\n Opção inválida.")
      time.sleep(3)
      os.system("cls || clear")














"""()

contador = 0
salario_maior_5k = 0
soma = 0
maior = 0
menor = 0

while True:
    print(
CÓDIGO | DESCRIÇÃO
       |
       |
       |
    )

    opcao = int(input("Informe seus dados."))
    
    match opcao:
        case 1 | "M" | "F":
        
        
         idade = int(input("Digite sua idade:"))
         
       
         sexo = str(input("Qual o seu sexo:")).upper()

        

         salario = int(input("qual seu salário mensal:"))
         contador += 1
         soma += salario

         media = contador / soma

       
         maior = max(maior, idade)
         menor = min(menor, idade)
        

         
         

         if salario >= 5000:
          salario_maior_5k += soma 
          print(salario_maior_5k)
         else:
            print("ok")
    
        case 2:
       
  
         print(media)
         print(f"A pessoa de maior idade do grupo tem {maior}")
         print(f"A pessoa de maior idade do grupo tem {menor}")
       
        
         print(f"A pessoa de maior idade do grupo tem {maior}")
         print(f"A pessoa de maior idade do grupo tem {menor}")

         
         

         print(salario_maior_5k)
        
          
        
    
        
        case 3:
         print("sair")

        case _:
         print("")
        
"""