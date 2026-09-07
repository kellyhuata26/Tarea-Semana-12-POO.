class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        valor = float(valor)

        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = valor

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        valor = int(valor)

        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._stock = valor

    def vender(self, cantidad: int) -> None:
        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("No existe suficiente stock.")

        self._stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria} | "
            f"Stock: {self.stock}"
        )