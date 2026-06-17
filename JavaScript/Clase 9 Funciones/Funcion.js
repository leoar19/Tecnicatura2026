// Evitar repetir tu codigo
// Dry don't repeat yourself
let days = 1;

switch(days) {
    case 1:
        console.log('Hoy es Lunes');
        break;
    case 2:
        console.log('Hoy es Martes');
        break;
    case 3:
        console.log('Hoy es Miércoles');
        break;
    case 4:
        console.log('Hoy es Jueves');
        break;
    case 5:
        console.log('Hoy es Viernes');
        break;
    case 6:
        console.log('Hoy es Sábado');
        break;
    case 7:
        console.log('Hoy es Domingo');
        break;
    default:
        console.log('Error en el ingreso del dia de la semana');
        break;
}

// Esta es la version mejorada

let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];

function getDay(n) {
    if (n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));