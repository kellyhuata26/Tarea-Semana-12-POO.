import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


RUTA_BASE = os.path.dirname(os.path.abspath(__file__))

RUTA_PRODUCTOS = os.path.join(
    RUTA_BASE,
    "datos",
    "productos.json"
)

RUTA_USUARIOS = os.path.join(
    RUTA_BASE,
    "datos",
    "usuarios.json"
)

RUTA_VENTAS = os.path.join(
    RUTA_BASE,
    "datos",
    "ventas.json"
)


def mostrar_menu() -> None:
    print("\n" + "=" * 50)
    print("        RESTAURANTE APP - SEMANA 11")
    print("=" * 50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Realizar venta")
    print("6. Consultar ventas de un usuario")
    print("7. Salir")


def main() -> None:

    os.makedirs(
        os.path.join(RUTA_BASE, "datos"),
        exist_ok=True
    )

    productos = ArchivoServicio.cargar_productos(RUTA_PRODUCTOS)
    usuarios = ArchivoServicio.cargar_usuarios(RUTA_USUARIOS)
    ventas = ArchivoServicio.cargar_ventas(RUTA_VENTAS)

    restaurante = Restaurante(
        productos,
        usuarios,
        ventas
    )

    print("\nDatos cargados correctamente.")
    print(f"Productos recuperados: {len(productos)}")
    print(f"Usuarios recuperados: {len(usuarios)}")
    print(f"Ventas recuperadas: {len(ventas)}")

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ").strip()

        # ======================================
        # REGISTRAR PRODUCTO
        # ======================================

        if opcion == "1":
            try:
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: "))
                categoria = input("Categoría: ").strip()
                stock = int(input("Stock inicial: "))

                producto = Producto(
                    codigo,
                    nombre,
                    precio,
                    categoria,
                    stock
                )

                if restaurante.registrar_producto(producto):
                    ArchivoServicio.guardar_productos(
                        RUTA_PRODUCTOS,
                        restaurante.obtener_productos()
                    )
                    print("Producto registrado correctamente.")
                else:
                    print("Ya existe un producto con ese código.")

            except ValueError as error:
                print(f"Error: {error}")

        # ======================================
        # LISTAR PRODUCTOS
        # ======================================

        elif opcion == "2":

            productos = restaurante.listar_productos()

            if not productos:
                print("No existen productos registrados.")
            else:
                print("\n--- PRODUCTOS ---")

                for producto in productos:
                    print(producto)

        # ======================================
        # REGISTRAR USUARIO
        # ======================================

        elif opcion == "3":
            try:
                identificacion = input("Identificación: ").strip()
                nombre = input("Nombre: ").strip()
                correo = input("Correo electrónico: ").strip()

                usuario = Usuario(
                    identificacion,
                    nombre,
                    correo
                )

                if restaurante.registrar_usuario(usuario):
                    ArchivoServicio.guardar_usuarios(
                        RUTA_USUARIOS,
                        restaurante.obtener_usuarios()
                    )
                    print("Usuario registrado correctamente.")
                else:
                    print("Ya existe un usuario con esa identificación.")

            except ValueError as error:
                print(f"Error: {error}")

        # ======================================
        # LISTAR USUARIOS
        # ======================================

        elif opcion == "4":

            usuarios = restaurante.listar_usuarios()

            if not usuarios:
                print("No existen usuarios registrados.")
            else:
                print("\n--- USUARIOS ---")

                for usuario in usuarios:
                    print(usuario)

        # ======================================
        # REALIZAR VENTA
        # ======================================

        elif opcion == "5":

            try:
                identificacion = input(
                    "Identificación del usuario: "
                ).strip()

                codigo = input(
                    "Código del producto: "
                ).strip()

                cantidad = int(
                    input("Cantidad a comprar: ")
                )

                usuario = restaurante.buscar_usuario(
                    identificacion
                )

                if usuario is None:
                    print("Error: el usuario no existe.")
                    continue

                producto = restaurante.buscar_producto(
                    codigo
                )

                if producto is None:
                    print("Error: el producto no existe.")
                    continue

                if cantidad <= 0:
                    print(
                        "Error: la cantidad debe ser mayor que cero."
                    )
                    continue

                if producto.stock < cantidad:
                    print(
                        "Error: stock insuficiente."
                    )
                    continue

                venta_realizada = restaurante.vender_producto(
                    codigo,
                    identificacion,
                    cantidad
                )

                if venta_realizada:

                    ArchivoServicio.guardar_productos(
                        RUTA_PRODUCTOS,
                        restaurante.obtener_productos()
                    )

                    ArchivoServicio.guardar_ventas(
                        RUTA_VENTAS,
                        restaurante.obtener_ventas()
                    )

                    print("Venta realizada correctamente.")
                    print(
                        f"Stock restante de {producto.nombre}: "
                        f"{producto.stock}"
                    )

                else:
                    print("No fue posible realizar la venta.")

            except ValueError:
                print(
                    "Error: ingrese una cantidad numérica válida."
                )

        # ======================================
        # CONSULTAR VENTAS POR USUARIO
        # ======================================

        elif opcion == "6":

            identificacion = input(
                "Identificación del usuario: "
            ).strip()

            usuario = restaurante.buscar_usuario(
                identificacion
            )

            if usuario is None:
                print("El usuario no existe.")
                continue

            ventas_usuario = (
                restaurante.consultar_ventas_usuario(
                    identificacion
                )
            )

            if not ventas_usuario:
                print(
                    "El usuario no tiene ventas registradas."
                )
            else:
                print(
                    f"\n--- VENTAS DE {usuario.nombre} ---"
                )

                for venta in ventas_usuario:

                    producto = restaurante.buscar_producto(
                        venta.producto_codigo
                    )

                    nombre_producto = (
                        producto.nombre
                        if producto is not None
                        else "Producto no encontrado"
                    )

                    print(
                        f"Producto: {nombre_producto} | "
                        f"Código: {venta.producto_codigo} | "
                        f"Cantidad: {venta.cantidad}"
                    )

        # ======================================
        # SALIR
        # ======================================

        elif opcion == "7":
            print(
                "\nGracias por utilizar Restaurante App."
            )
            break

        else:
            print(
                "Opción inválida. Intente nuevamente."
            )


if __name__ == "__main__":
    main()