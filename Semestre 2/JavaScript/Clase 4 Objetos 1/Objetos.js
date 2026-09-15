let x = 10; // variable de tipo primitiva
console.log(x.length); // undefined, no encontramos propiedades asociadas a este valor
console.log('Tipos primitivos');
// Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido; //this apunta al objeto dentro del bloque existente
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