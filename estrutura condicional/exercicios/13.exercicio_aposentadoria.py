coloborador_matricula = int(input("Digite seu numero de matricula:"))
ano_atual = int(input("Digite ano atual:"))
ano_nascimento = int(input("Digite sua data de nascimento:"))
tempo_trabalhoa_ano = int(input("Digite o tempo de trabalho:"))
 
idade = ano_nascimento - ano_atual  
if idade >= 65 or tempo_trabalhoa_ano >= 30:
   resultado = "Requerer aponsentadoria"
else:
   resultado = "Não requerer aponsentadoria"

  

