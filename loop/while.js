// laço de repetição for de 1 ate 5

for (let i = 1; i <= 5; i++) {
    console.log(i);
}



// laço de repetição : While 

let i = 1

while (i <= 5) {
    console.log(i)
    i++
}



// laçao de repetição : Do while

let j =  1;

do {
    console.log(j)
    j++ 
} while (j <= 5)


for (let i = 1; i <= 2; i++) {
    let aluno = parseFloat("Digite sua nota:"); 

    if (aluno >= 7) {
        console.log("NOTA BOA");
    } else if (aluno >= 5 && aluno < 7) {
        console.log("NOTA REGULAR");  
    } else {
        console.log("NOTA RUIM");
    }
}