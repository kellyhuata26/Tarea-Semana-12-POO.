class Venta:
    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ):
        if not usuario_id or not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")

        if not producto_codigo or not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    def __str__(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )