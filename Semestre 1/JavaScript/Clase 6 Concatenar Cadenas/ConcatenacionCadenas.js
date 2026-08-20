var nombre = "Jose";
var apellido = "Montes";
var nombreCompleto = nombre +" " + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = "Leo" + " " + "Araya";
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el num como str.
console.log(juntos);
juntos = nombre + (78 + 17); //Se puede diferenciar con parentesis
console.log(juntos)
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;
console.log(nombre);

// Hoy ya no se usa var, se usa let y const.
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes"; // Una constante no se puede modificar.
console.log(apellido2);