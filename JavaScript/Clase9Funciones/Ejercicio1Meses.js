// Hacer un ejercicio similar al que esta hecho, pero ahora con los meses del año, debes
// hacerlo con la estructura switch y luego con la funcion en la opcion mejorada.
//Estructura switch

let months = 1;

switch(months) {
    case 1:
        console.log('Estamos en el mes 1: Enero');
        break;
    case 2:
        console.log('Estamos en el mes 2: Febrero');
        break;
    case 3:
        console.log('Estamos en el mes 3: Marzo');
        break;
    case 4:
        console.log('Estamos en el mes 4: Abril');
        break;
    case 5:
        console.log('Estamos en el mes 5: Mayo');
        break;
    case 6:
        console.log('Estamos en el mes 6: Junio');
        break;
    case 7:
        console.log('Estamos en el mes 7: Julio');
        break;
    case 8:
        console.log('Estamos en el mes 8: Agosto');
        break;
    case 9:
        console.log('Estamos en el mes 9: Septiembre');
        break;
    case 10:
        console.log('Estamos en el mes 10: Octubre');
        break;
    case 11:
        console.log('Estamos en el mes 11: Noviembre');
        break;
    case 12:
        console.log('Estamos en el mes 12: Diciembre');
        break;
    default:
        console.log('No ingresaste un mes válido (debe ser 1-12)');
        break;
}

// Estructura de funcion

let monthsArray = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
    'Octubre', 'Noviembre', 'Diciembre'
]

function getMonth(n) {
    if (n < 1 || n > 12) {
        throw new Error ('out of range');
    }
    return monthsArray[n-1];
}
console.log(getMonth(5));