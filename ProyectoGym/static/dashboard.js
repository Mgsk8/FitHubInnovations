// dashboard.js

// Este script puede ser compartido por todas las vistas que utilicen el dashboard
// Simplemente define la lógica para cargar dinámicamente el contenido del dashboard

// Obtener el contenedor del dashboard
var dashboardContainer = document.getElementById("dashboard-container");

// Dependiendo de la vista actual, llenar el contenido del dashboard
// Esto podría ser más sofisticado, dependiendo de las necesidades específicas del proyecto
switch(window.location.pathname) {
    case "/prueba.html":
        dashboardContainer.innerHTML = "<h2>Bienvenido al sistema</h2>";
        break;
    case "/usuarios.html":
        dashboardContainer.innerHTML = "<h2>Lista de Usuarios</h2><table><tr><th>Nombre</th><th>Email</th></tr><tr><td>Usuario 1</td><td>usuario1@example.com</td></tr><tr><td>Usuario 2</td><td>usuario2@example.com</td></tr></table>";
        break;
    // Agregar más casos según sea necesario para otras vistas
    default:
        // Si no coincide con ninguna vista conocida, dejar el dashboard vacío o mostrar un mensaje de error
        //dashboardContainer.innerHTML = "<h2>Dashboard</h2>";
}
