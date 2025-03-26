


contador = 0
salario_maior_5k = 0

while True:
    print("""
CÓDIGO | DESCRIÇÃO
       |
       |
       |
    """)

    opcao = int(input("Informe seus dados."))
    
    match opcao:
        case 1:
        
        
         idade = int(input("Digite sua idade:"))
         
         sexo = input("Qual o seu sexo:")

         salario = float(input("qual seu salário mensal:"))
         contador += 1


        case 2:
         contador += salario
         media = contador / salario
        
        case 3:
         maior_idade = min(idade)
         menor_idade = max(idade)

        case 4:
        
        if salario >= 5000
    