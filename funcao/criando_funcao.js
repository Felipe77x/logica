// Crirando uma função

function somar(a, b) {
    return a + b;
}

function subtrair(a, b) {
    return a - b;
}

function multiplicar(a,b) {
    return a * b;
}

function divisao(a,b) {
    return a * b;
}

// chamando a função 
// Adicionar o resultado da função na constante

const subtrcao = subtrair(50,30)
const soma = somar(50, 30)
const multiplicacao = multiplicar(50,10)
const dividir = divisao(50,10)
// Mostra o conteúdo da constante

console.log(`Soma: ${soma}`)
console.log(`subtrair: ${subtrcao}`)
console.log(`Multiplicação: ${multiplicacao}`)
console.log(`Divisão: ${dividir}`)