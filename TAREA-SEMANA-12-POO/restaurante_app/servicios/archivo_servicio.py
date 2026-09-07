import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    @staticmethod
    def guardar_productos(ruta: str, productos: list[Producto]) -> None:
        datos = [producto.a_diccionario() for producto in productos]

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)

        except PermissionError:
            print("Error: no tiene permisos para guardar productos.")

    @staticmethod
    def cargar_productos(ruta: str) -> list[Producto]:
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            productos = []

            for dato in datos:
                try:
                    producto = Producto(
                        dato["codigo"],
                        dato["nombre"],
                        dato["precio"],
                        dato["categoria"],
                        dato["stock"]
                    )
                    productos.append(producto)

                except KeyError as error:
                    print(f"Error: falta la clave {error} en un producto.")

                except ValueError as error:
                    print(f"Error al reconstruir un producto: {error}")

            return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: productos.json contiene un formato JSON inválido.")
            return []

        except PermissionError:
            print("Error: no tiene permisos para leer productos.")
            return []

    @staticmethod
    def guardar_usuarios(ruta: str, usuarios: list[Usuario]) -> None:
        datos = [usuario.a_diccionario() for usuario in usuarios]

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)

        except PermissionError:
            print("Error: no tiene permisos para guardar usuarios.")

    @staticmethod
    def cargar_usuarios(ruta: str) -> list[Usuario]:
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            usuarios = []

            for dato in datos:
                try:
                    usuario = Usuario(
                        dato["identificacion"],
                        dato["nombre"],
                        dato["correo"]
                    )
                    usuarios.append(usuario)

                except KeyError as error:
                    print(f"Error: falta la clave {error} en un usuario.")

                except ValueError as error:
                    print(f"Error al reconstruir un usuario: {error}")

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: usuarios.json contiene un formato JSON inválido.")
            return []

        except PermissionError:
            print("Error: no tiene permisos para leer usuarios.")
            return []

    @staticmethod
    def guardar_ventas(ruta: str, ventas: list[Venta]) -> None:
        datos = [venta.a_diccionario() for venta in ventas]

        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)

        except PermissionError:
            print("Error: no tiene permisos para guardar ventas.")

    @staticmethod
    def cargar_ventas(ruta: str) -> list[Venta]:
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            ventas = []

            for dato in datos:
                try:
                    venta = Venta(
                        dato["usuario_id"],
                        dato["producto_codigo"],
                        dato["cantidad"]
                    )
                    ventas.append(venta)

                except KeyError as error:
                    print(f"Error: falta la clave {error} en una venta.")

                except ValueError as error:
                    print(f"Error al reconstruir una venta: {error}")

            return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: ventas.json contiene un formato JSON inválido.")
            return []

        except PermissionError:
            print("Error: no tiene permisos para leer ventas.")
            return []