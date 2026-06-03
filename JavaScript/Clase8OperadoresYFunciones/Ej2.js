// Calcular estacion del año
let mesDelAnio = parseInt(prompt('Ingresa un mes del año: '));
let estacion;
if (mesDelAnio >=1 && mesDelAnio <= 12) {
    if (mesDelAnio <= 3) {
        estacion = 'Verano';
    }
    else if (mesDelAnio <= 6) {
        estacion = 'Otoño';
    }
    else if (mesDelAnio <= 9) {
        estacion = 'Invierno';
    }
    else {
        estacion = 'Primavera';
    }

    console.log(`Estas en ${estacion}`);
} else {
    console.log('No ingresaste un mes valido');
}

// Con switch
// No solo se pueden utilizar numeros, sino tambien cadenas
// switch(mesDelAnio) {
//     case 1: case 2: case 3:
//         estacion = 'Verano';
//         break;
//     case 4: case 5: case 6:
//         estacion = 'Otoño';
//         break;
//     case 7: case 8: case 9:
//         estacion = 'Invierno';
//         break;
//     case 10: case 11: case 12:
//         estacion = 'Primavera';
//         break;
//     default:
//         estacion = 'Valor incorrecto';
// }
// console.log(`Estas en ${estacion}`);