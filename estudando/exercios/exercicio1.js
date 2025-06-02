
const readline = require('readline-sync')

let valor1 = readline.questionFloat('Digite uma nota:')
let valor2 = readline.questionFloat('Digite uma nota:')
let valor3 = readline.questionFloat('Digite uma nota:')



if (valor1 + valor2 > valor3) {
    console.log('A é B maior que C')
}else if (valor1 + valor2 < c){
    console.log('A é B menor que C')
}else{
    console.log('Valor errado !!!')
}

