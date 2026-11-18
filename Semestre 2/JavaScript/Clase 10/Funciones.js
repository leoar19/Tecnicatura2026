// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)
function validatePassword(password) {
    // Cada regla se evalúa por separado para que el código sea autoexplicativo
    // y si algún día falla un test, será fácil ver qué condición no se cumplió.
    const tieneLongitudMinima = password.length >= 8;
    const tieneNumero = /\d/.test(password); // \d = cualquier dígito 0-9, .test() = true si encuentra
    const tieneMayuscula = /[A-Z]/.test(password); // alguna letra A-Z. No valida tildes.

    // Solo es válida si las TRES condiciones son verdaderas.
    // Se podría usar if/else, pero && es más directo y devuelve el boolean.
    return tieneLongitudMinima && tieneNumero && tieneMayuscula;
}

console.log(validatePassword("Abc12345")); // true
console.log(validatePassword("weak")); // false
console.log(validatePassword("Ábc12345")); // false (tilde en A)
console.log(validatePassword("abcdefgh1")); // false (sin mayúscula)
console.log(validatePassword("Abcdefgh"));  // false (sin número)

// Ejercicio 2: Crear un sistema simple de gestión de tareas
function createTaskManager() {
    const tasks = []; // Array donde se acumulan las tareas
    let id = 1; // Contador

    return {
        // Añade una nueva tarea al gestor.
        // El id se autoincrementa con id++.
        // Toda tarea nueva empieza con completed: false
        // text - Descripción de la tarea.
        addTask(text) {
            tasks.push({ id: id++, text, completed: false });
        },

        // Marca una tarea como completada según el id.
        // Si el id no existe muestra un mensaje.
        // taskId - id de la tarea a completar.
        completeTask(taskId) {
            // find devuelve la primera tarea que coincida con el id, o undefined si ninguna coincide.
            const t = tasks.find(t => t.id === taskId);

            // Si no se encontró la tarea, muestra un mensaje y sale con return.
            if (!t) return console.log(`No existe la tarea ${taskId}`);
            t.completed = true;
        },

        // Devolvemos una copia de cada tarea (spread {...t})
        listTasks() {
            return tasks.map(t => ({ ...t }));
        }
    };
}

// Uso:

const myTasks = createTaskManager();
myTasks.addTask("Aprender JavaScript"); // id 1, completed: false
myTasks.addTask("Hacer ejercicio"); // id 2, completed: false

myTasks.completeTask(1); // marca aprender javascript como completada.
console.log(myTasks.listTasks());

myTasks.completeTask(99); // Muestra un mensaje de que no existe