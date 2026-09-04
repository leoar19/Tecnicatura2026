# Clase 1 Portafolio: HTML etiquetas: `<header>`, `<nav>` y `<meta>`
## `<header>` (Cabecera)
Representa el bloque introductorio de una página o de una sección específica.
No se debe confundir con `<head>` que contiene metadatos invisibles. El `<header>` es visible para el usuario.
> ¿Qué suele contener?
* Logotipos
* Títulos principales
* Subtítulos
* Menú de navegación (`<nav>`)
* Buscador

### Ejemplo básico
```html
<header>
    <h1>Mi Portafolio de Programación</h1>
    <p>Aprendiendo HTML y CSS desde cero</p>
    <!-- Aquí suele ir el nav -->
</header>
```

## `<nav>` (Navegación)
Define un bloque de enlaces que sirven para la navegación principal del sitio web. Su objetivo es agrupar los accesos a las distintas páginas o secciones internas.
> ¿Qué suele contener?
* Menús principales
* Tablas de contenido
* Enlaces a redes sociales
> NO TODOS los enlaces deben estar dentro de un `<nav>`, solo los más importantes. Si se tiene un enlace suelto es mejor usar un `<a>` común.

### Ejemplo básico
```html
<nav>
    <ul>
        <li><a href="#inicio">Inicio</a></li>
        <li><a href="#proyectos">Proyectos</a></li>
        <li><a href="#contacto">Contacto</a></li>
    </ul>
</nav>
```

## `<meta>` (Metadatos)
No es visible en la interfaz gráfica. Se coloca dentro del `<head>` y sirve para darle instrucciones al navegador o a los motores de búsqueda sobre cómo manejar nuestra página.
> ¿Para qué sirve?
* Definir el juego de caracteres (acentos y ñ)
* Ajustar la página para dispositivos móviles (viewport)
* Dar una descripción para el SEO

### Ejemplos básicos
```html
<head>
    <!-- 1. Codificación de caracteres (permite usar tildes y la Ñ) -->
    <meta charset="UTF-8">

    <!-- 2. Configuración para vista en dispositivos móviles (¡OBLIGATORIO para que se vea bien!) -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- 3. Descripción para buscadores (SEO) -->
    <meta name="description" content="Resumen de etiquetas HTML para la tecnicatura en programación.">

    <!-- 4. Autor de la página -->
    <meta name="author" content="Nombre">
</head>
```