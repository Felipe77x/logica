

const readline = require('readline-sync')
let par_ou_impar = readline.questionFloat('Digite uma nota:')


if (par_ou_impar % 2 == 0 ) {
    console.log('O numero é par ')
} else if (par_ou_impar % 2 == 1) {
    console.log('O numero é impar')
}else{
    console.log('Error')
}