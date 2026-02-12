from pizzeria import Pizzeria
from pedido import Pedido
from pizza import Pizza
from ingredientes.queso import Queso
from ingredientes.carne import Carne
from ingredientes.vegetal import Vegetal

def main():
    pizzeria = Pizzeria()
    pedido = Pedido()

    while True:
        pizzeria.mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            pizza = Pizza("Personalizada")
            # TODO: añadir ingredientes
            # muestra al usuario opciones para que elija qué ingredientes quiere añadir a su pizza, 
            # hasta que elija la opción de terminar pizza
            # Por ejemplo, así añadiría Queso y después terminaría la pizza.
            
            """
                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
                Elige ingrediente: 1

                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
                Elige ingrediente: 0
            """
            pedido.add_pizza(pizza)
        elif opcion == "2":
            pedido.mostrar_pedido()
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()

