
valor_produto = float(("Informe o valor do produto:")) 
forma_pagamento = input("Digite a forma de pagamento:")

match forma_pagamento:
    case 1:
      desconto = valor_produto * .10