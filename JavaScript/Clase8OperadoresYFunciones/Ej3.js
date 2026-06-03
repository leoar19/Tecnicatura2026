// Hora del dia
// En base a la hora del dia, qué estamos haciendo como: desayunar, trabajar, estudiar, cenar, etc.
let hora = parseInt(prompt('Ingresa la hora (0-23): '));
if (hora >= 0 && hora <= 23) {
    let actividad;
    if (hora <= 8) {
        actividad = 'Estoy durmiendo';
    } else if (hora <= 9) {
        actividad = 'Estoy desayunando';
    } else if (hora <= 10) {
        actividad = 'Estoy en mi tiempo libre';
    } else if (hora <= 13) {
        actividad = 'Estudio portugués';
    } else if (hora <= 14) {
        actividad = 'Estoy almorzando';
    } else if (hora <= 15) {
        actividad = 'Estoy descansando';
    } else if (hora <= 18) {
        actividad = 'Estudio programación';
    } else if (hora <= 22) {
        actividad = 'Estoy en clases';
    } else {  // hora 23
        actividad = 'Cena y ducha';
    }
    
    console.log(`Hora: ${hora}hs. Actividad: ${actividad}`);
} else {
    console.log('Ingresa una hora válida (0-23)');
}