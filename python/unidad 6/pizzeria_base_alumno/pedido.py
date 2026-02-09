class Pedido:
    def __init__(self):
        self.__pizzas = []

    def add_pizza(self, pizza):
        self.__pizzas.append(pizza)

    def mostrar_pedido(self):
        for pizza in self.__pizzas:
            print(pizza.get_nombre())
            print(pizza.imprimir_ascii())
