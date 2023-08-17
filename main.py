class Cajero:
    def __init__(self):
        self.inventario = {}
        self.saldo = 0.0

    def registrar_compra(self, producto, cantidad, precio):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad
        self.saldo -= cantidad * precio
        print(f"Compra registrada: {cantidad} {producto}(s) a ${precio} cada uno.")

    def registrar_venta(self, producto, cantidad, precio):
        if producto in self.inventario and self.inventario[producto] >= cantidad:
            self.inventario[producto] -= cantidad
            self.saldo += cantidad * precio
            print(f"Venta registrada: {cantidad} {producto}(s) a ${precio} cada uno.")
        else:
            print("No hay suficiente inventario para realizar la venta.")

    def ver_inventario(self):
        print("\nInventario:")
        for producto, cantidad in self.inventario.items():
            print(f"{producto}: {cantidad}")
        print(f"Saldo actual: ${self.saldo}\n")

def main():
    cajero = Cajero()

    while True:
        print("Bienvenido al cajero")
        print("1. Registrar compra")
        print("2. Registrar venta")
        print("3. Ver inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio por unidad: "))
            cajero.registrar_compra(producto, cantidad, precio)
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio por unidad: "))
            cajero.registrar_venta(producto, cantidad, precio)
        elif opcion == "3":
            cajero.ver_inventario()
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()