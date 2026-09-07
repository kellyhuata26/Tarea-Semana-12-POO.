from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    def __init__(
        self,
        productos: list[Producto] | None = None,
        usuarios: list[Usuario] | None = None,
        ventas: list[Venta] | None = None
    ):
        self._productos = productos if productos is not None else []
        self._usuarios = usuarios if usuarios is not None else []
        self._ventas = ventas if ventas is not None else []

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    # =========================
    # VENTAS
    # =========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return self._ventas.copy()

    # =========================
    # COLECCIONES PARA JSON
    # =========================

    def obtener_productos(self) -> list[Producto]:
        return self._productos.copy()

    def obtener_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def obtener_ventas(self) -> list[Venta]:
        return self._ventas.copy()