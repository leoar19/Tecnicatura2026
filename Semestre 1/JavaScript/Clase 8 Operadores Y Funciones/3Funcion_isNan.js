// Funcion isNan
let miNumero = '10';
console.log(typeof miNumero);
let edad = Number(miNumero); // Esta es una función
console.log(typeof edad);
if (isNaN(edad)) { // Devuelve un resultado booleano
    console.log('Esta variable no contiene solo numeros')
} else {
if (edad >= 18) {
    console.log('Puede votar');
} else {
    console.log('Es demasiado joven para votar');
    }
}

let resultado = edad >= 18 ? 'Puede votar' : 'Muy joven para votar';
console.log(resultado);