
function calcular_nota() {
const readline = require('readline-sync')

let nota1 = readline.questionFloat('Digite uma nota:')
let nota2 = readline.questionFloat('Digite uma nota:')

let nota_final;

    if (nota1 === nota2) {
        nota_final = nota1 + nota2;
    } else {
        nota_final = nota1 * nota2;
    }





console.log(`Nota_final ${nota_final}`)



}





calcular_nota();