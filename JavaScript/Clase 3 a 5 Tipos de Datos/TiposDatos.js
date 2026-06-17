//Tipos de Datos en JS
//Recordar que las variables en JS son dinamicas
//Tipo String
var nombre = "Leonel";
console.log(typeof nombre); //typeof sirve para saber de que tipo es la variable u objeto
nombre = 7;
console.log(typeof nombre);
nombre = 12.5;
console.log(typeof nombre);
//Tipo Numerico
var numero = 3000;
console.log(numero);

var objeto = {
  //Tipo objeto
  nombre: "Leonel",
  apellido: "Araya",
  telefono: "123456789",
};
console.log(objeto);

//Tipos de datos Boolean
var bandera = true;
console.log(bandera);

//Tipo de dato Funcion
//Permite realizar una tarea, se pueden reutilizar las veces necesarias llamandola.
function miFuncion() {}
console.log(typeof miFuncion);

//Tipo de dato Symbol
//Podemos ingresar una cadena
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato Clase, también son funciones
class Persona {
  constructor(nombre, apellido) {
    this.nombre = nombre;
    this.apellido = apellido;
  }
}

console.log(typeof Persona);

//Tipo de dato undefined
//Al definir cualquier tipo de variable cuando no está inicializada.
var x;
console.log(x);

x = undefined;
console.log(typeof x);

// null = Ausencia de un valor.
//No es un tipo de dato pero su origen es object.
var y = null;
console.log(y);
console.log(typeof y);

//Tipo de dato Array y Empty String
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z); //Cadena vacía (Empty String)
console.log(typeof z);