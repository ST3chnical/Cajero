class ATM:
    def __init__(self):
        self.inventory = {}
        self.balance = 0.0

    def register_purchase(self, product, quantity, price):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        self.balance -= quantity * price
        print(f"Compra registrada: {quantity} {product}(s) a ${price} cada uno.")

    def register_sale(self, product, quantity, price):
        if product in self.inventory and self.inventory[product] >= quantity:
            self.inventory[product] -= quantity
            self.balance += quantity * price
            print(f"Venta registrada: {quantity} {product}(s) a ${price} cada uno.")
        else:
            print("No hay suficiente inventario para realizar la venta.")

    def see_inventory(self):
        print("\nInventario:")
        for product, quantity in self.inventory.items():
            print(f"{product}: {quantity}")
        print(f"Saldo actual: ${self.balance}\n")


def main():
    atm = ATM()

    while True:
        print("Bienvenido al atm")
        print("1. Registrar compra")
        print("2. Registrar venta")
        print("3. Ver inventario")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            product = input("Ingrese el nombre del producto: ")
            quantity = int(input("Ingrese la quantity: "))
            price = float(input("Ingrese el price por unidad: "))
            atm.register_purchase(product, quantity, price)
        elif option == "2":
            product = input("Ingrese el nombre del producto: ")
            quantity = int(input("Ingrese la quantity: "))
            price = float(input("Ingrese el price por unidad: "))
            atm.register_sale(product, quantity, price)
        elif option == "3":
            atm.see_inventory()
        elif option == "4":
            print("Gracias por usar el atm.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
