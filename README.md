---

# Sof Shoes 👟

Sof Shoes es una aplicación web que te permite explorar nuestra tienda de zapatillas. Además, ofrece una serie de funciones y enlaces que facilitan la búsqueda en la base de datos, la adición de productos, clientes, proveedores, pedidos y más.
Tambien permite hacer un logeo de usuarios y permite dar permisos a los mismos en caso de querer ser administrador de la web.

## Requisitos 📋

Antes de comenzar, asegúrate de tener los siguientes requisitos en tu entorno de desarrollo:

- Python 3.11.5 64-bit 🐍
- Dependencias de Django:
  - asgiref==3.7.2
  - certifi==2023.7.22
  - distlib==0.3.7
  - Django==4.2.4
  - filelock==3.12.3
  - pipenv==2023.9.1
  - platformdirs==3.10.0
  - sqlparse==0.4.4
  - tzdata==2023.3
  - virtualenv==20.24

## Instalación 🚀

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. Clona el repositorio desde GitHub.
2. Crea un entorno virtual para tu proyecto.
3. Instala las dependencias utilizando Pipenv o tu gestor de paquetes preferido.
4. Configura las variables de entorno si es necesario.
5. Ejecuta las migraciones de Django para crear la base de datos.
6. Inicia el servidor desde la terminal de Visual Studio Code o con el comando `python manage.py runserver`.

## Uso 🌟

La aplicacion ofrece varias secciones en las cuales podras registrarte, logearte, etc.

- **sof-shoes/**: Página de inicio.
- **lista-de-productos/**: Lista de productos disponibles.
- **marcas/**: Vista de marcas.
- **about-us/**: Vista donde podras conocer mas acerca de mi.
- **contacto/**: Vista de contacto.
---> En los botones de la aplicacion podras hacer otras acciones, ofrece las siguientes:
- **Login**: Permitira logearse en la pagina web.
- **Registrarse aqui**: Este estara dentro de Login y permite registrarse en caso de no estarlo.
- **Perfil**: Permite ver su Perfil de Usuario.
- **Editar Perfil**: Este estara dentro de Perfil y permite editar o agregar datos a su perfil; nombre de usuario, e-mail, descripcion, link a pagina web, avatar y contraseña.
- **Salir**: Para salir del usuario.
- **Editar**: Este boton esta disponible SOLO para administradores de la web y esta disponible en la solapa de Productos, este permite editar el producto, su nombre, sus talles y su precio.
- **Eliminar**: Este boton esta disponible SOLO para administradores de la web y esta disponible en la solapa de Productos, este permite eliminar el producto.
- **Agregar Producto**: Este boton esta disponible SOLO para administradores de la web y esta disponible en la solapa de Productos, este permite agregar un producto.
---> Ademas esta aplicacion cuenta con un NavBar por el cual podras manejar todas las url disponibles y un footer para interactuar con un instagram, faceebok, twitter y otros.

## Contribución 🤝

Este proyecto esta desarrollado con el objetivo de brindar un proyecto final de alta calidad para el curso de Python orientado a Desarrollo Web en la plataforma de CoderHouse.

## ¿Necesitas Ayuda? 🤔

Si tienes alguna pregunta o necesitas asistencia técnica, no dudes en ponerte en contacto con nosotros en [agustinlucaspdl@gmail.com](mailto:agustinlucaspdl@gmail.com) 📧.

---
