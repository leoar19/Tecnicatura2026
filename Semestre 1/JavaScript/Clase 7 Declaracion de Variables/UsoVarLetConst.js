/*
Con var se puede reasignar en cualquier momento, este forma parte del ámbito global.
Un error es que se sobreescriba.
*/
var nombre = "Leo";
nombre = "Juan";
console.log(nombre);

function saludar() {
    var nombre3 = "Natalia";
    console.log(nombre3);
}
// console.log(nombre3) Aqui no lee el dato de la funcion

if (true) {
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo.
//Interpreta que la variable está definida, es un fallo.

/*
Let
Puede ser reasignada en cualquier momento, la diferencia es que su ambito es de bloque.
Solo disponible dentro de un bloque de llaves o dentro de una funcion.
*/
function saludar2() {
    let nombre2 = "Leo";
    console.log(nombre2);
}
//console.log(nombre2);

if (true) {
    let edad2 = 23;
    console.log(edad2);
}
//console.log(edad2);

/*
Const
Se utiliza para valores constantes que no pueden ser reasignados.
*/
const fechaNacimiento = 2002;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento) solo se ejecutaría el log anterior.