let x = 10; // variable de tipo primitiva
console.log(x.length); // undefined, no encontramos propiedades asociadas a este valor
console.log('Tipos primitivos');
// Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){ // antes de almacenar cualquier valor, lo primero es convertir a mayusculas
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido; //this apunta al objeto dentro del bloque existente
    },
    get nombreEdad(){ // metodo get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log('Ejecutando con un objeto');
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

// Otra forma de crear un objeto
console.log('Creamos un nuevo objeto');
let persona2 = new Object(); // Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono);

// Otra forma de acceder a las propiedades de un objeto
console.log(persona['apellido']); // Accedemos como si fuera un arreglo

// for in
console.log('Usamos el ciclo for in');
for(propiedad in persona) {
    console.log(propiedad);
    console.log(persona[propiedad]);
}

// Agregar/Eliminar propiedades
console.log('Cambiamos una propiedad y eliminamos un error');
persona.apellida = 'Betancud'; // Cambiamos dinamicamente un valor del objeto
delete persona.apellida; // Eliminamos el error
console.log(persona);

// Distintas formas de imprimir un objeto
// Numero 1: La mas sencilla es concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: Forma 1');
console.log(persona.nombre + ', ' + persona.apellido);

// Numero 2: A traves del ciclo for in
console.log('Distintas formas de imprimir un objeto: Forma 2');
for(nombrePropiedad in persona) {
    console.log(persona[nombrePropiedad]);
}

// Numero 3: La funcion Object.values() esta funcion regresa nuestro objeto como un arreglo
console.log('Distintas formas de imprimir un objeto: Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: Utilizaremos el metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto: Forma 4');
let personaString = JSON.stringify(persona); // convierte nuestro objeto en una cadena
console.log(personaString);

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){ // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function() {
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis'; // Modificamos el nombre
padre.telefono = '5492618282821' // Añadimos una propiedad
console.log(padre);
console.log(padre.nombreCompleto()); // Utilizamos la funcion

let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto());
console.log(madre.telefono); // No tiene telefono, la propiedad no esta definida

// Distintas formas de crear objetos 2
// Caso Objeto 1
let miObjeto = new Object(); // Esta es una opcion formal
// Caso Objeto 2
let miObjeto2 = {}; // Esta opcion es breve y recomendada

// Caso String 1
let miCadena1 = new String('Hola'); // Sintaxis formal
// Caso String 2
let miCadena2 = 'Hola'; // Sintaxis simplificada y recomendada

// Caso con Numeros 1
let miNumero = new Number(1); // Sintaxis formal, no recomendad
// Caso con Numeros 2
let miNumero2 = 1; // Sintaxis recomendada

// Caso Boolean 1
let miBoolean1 = new Boolean(false); // Formal
// Caso Boolean 2
let miBoolean2 = false; // Sintaxis recomendada

// Caso Arreglos 1
let miArreglo1 = new Array(); // Formal
// Caso Arreglos 2
let miArreglo2 = []; // Sintaxis recomendada

// Caso Function 1
let miFuncion1 = new function(){}; // Despues de new todo es considerado objeto
// Caso Function 2
let miFuncion2 = function(){}; // Notacion simplificada y recomendada

// Uso de prototype
Persona3.prototype.telefono = '2618383832';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492618383832';
console.log(madre.telefono);

// Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono) {
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
    //nombreCompleto2: function() { // Metodo apply
        //return this.nombre+' '+this.apellido;
    //}
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618484845'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618585856'));

// Metodo apply
//console.log(persona4.nombreCompleto2.apply(persona5)); // Carlos Lara
let arreglo = ['Ing.', '5492618686865'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));

// Con call simplemente pasamos los argumentos seguidos de una coma (,).
// Con apply pasamos un arreglo con todos los valores de los argumentos.