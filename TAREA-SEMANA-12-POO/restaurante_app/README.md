# Restaurante App - Semana 11

## Fundamentos de colecciones aplicados a relaciones, ventas y persistencia JSON

**Estudiante:** Kelly Daniela Tanguila Huatatoca  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 11  

---

## Descripción del proyecto

Este proyecto corresponde a la evolución de la aplicación `restaurante_app` desarrollada durante las semanas anteriores de la asignatura Programación Orientada a Objetos.

En esta Semana 11 se incorporan fundamentos de colecciones para representar relaciones y operaciones reales entre los objetos del sistema. La principal mejora implementada es el registro de ventas, donde un usuario registrado puede comprar un producto disponible.

El sistema controla el stock de los productos, registra cada venta y conserva la información mediante archivos JSON. De esta manera, los productos, usuarios y ventas pueden recuperarse después de cerrar y volver a ejecutar el programa.

---

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md