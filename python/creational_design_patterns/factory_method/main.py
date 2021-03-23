from abc import ABC


class Pizza(ABC):
    def __init__(self, pizza_name):
        self._pizza_name = pizza_name

    def get_name(self):
        return self._pizza_name

    @staticmethod
    def prepare():
        print('Preparing pizza...')

    @staticmethod
    def bake():
        print('Baking pizza...')

    @staticmethod
    def cut():
        print('Cutting pizza...')

    @staticmethod
    def box():
        print('Boxing pizza...')


class CheesePizza(Pizza):

    def bake(self):
        print('Baking cheese pizza for 10 minutes until all the cheese is melted!')


class VeggiePizza(Pizza):

    def prepare(self):
        print('Preparing veggie pizza with season vegetables!')


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        pizza = None
        if pizza_type == 'cheese':
            pizza = CheesePizza(pizza_name='cheese')
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        return pizza


class PizzaStore(ABC):
    def __init__(self, factory: PizzaFactory):
        self.__factory = factory

    def order_pizza(self, pizza_type: str):
        pizza = self.__factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == '__main__':
    store = PizzaStore(PizzaFactory)
    new_pizza = store.order_pizza('cheese')
    print('Ordered a {0} pizza'.format(new_pizza.get_name()))
