function positivo_negativo () {

const readline = require('readline-sync')
let negativoo_positivo = readline.questionFloat('Digite uma nota:')

if (negativoo_positivo > 0) {
    console.log('Numero positivo')
}else if (negativoo_positivo < 0) {
    console.log('Numero Negativo')
} else{
    console.log('Error')
}


}



positivo_negativo()