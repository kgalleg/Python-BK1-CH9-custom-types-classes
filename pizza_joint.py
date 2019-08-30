class Pizza:

    def __init__(self):
        # Establish the properties of each pizza
        # with a default value
        self.size = ""
        self.crust_type = ""
        self.toppings = []


    def add_topping (self, topping):
        self.toppings.append(topping)


    def print_order(self):
        topping_str = ' and '.join(self.toppings)
        print(f'I would like a {self.size}, {self.crust_type} pizza with {topping_str}')

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust_type = "cheesy crust"
meat_lovers.add_topping("pepperoni")
meat_lovers.add_topping("olives")
meat_lovers.print_order()

veggy = Pizza()
veggy.size = 12
veggy.crust_type = "thin/glutten free crust"
veggy.add_topping("pinepple")
veggy.add_topping("green peppers")
veggy.print_order()


