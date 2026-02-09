class Pizzeria:
    def mostrar_menu(self):
        print("1. Crear pizza")
        print("2. Ver pedido")
        print("3. Salir")
    
    def mostrar_pedido(self, pizza):
        print("Tu pedido:")
        print(pizza.imprimir_ascii())   

