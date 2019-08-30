import datetime

class Building:

    def __init__(self, address, stories):
        # Establish the properties of each building
        # with a default value
        self.designer = "Karla Gallegos"
        self.date_constructed = 0
        self.owner = ""
        self.address = address
        self.stories = stories


    def construct (self):
        self.date_constructed = datetime.datetime.now()


    def purchase(self, owner):
        self.owner = owner

    def building_info (self):
        print(f'{self.address} was purchased by {self.owner} on {(self.date_constructed).strftime("%x")} and has {self.stories} stories.')


eight_zero_zero = Building("800 8th Street", 12)
eight_zero_zero.purchase("Richard LeFrak")
eight_zero_zero.construct()
eight_zero_zero.building_info()

nine_one_four = Building("914 Reliance Drive", 11)
nine_one_four.purchase("Bob Builder")
nine_one_four.construct()
nine_one_four.building_info()

three_zero_one = Building("301 Plus Park", 3)
three_zero_one.purchase("May Fields")
three_zero_one.construct()
three_zero_one.building_info()

lwy_building = Building("LifeWay Building Downtown Nash", 219)
lwy_building.purchase("Mark Cuban")
lwy_building.construct()
lwy_building.building_info()

monkey_temple = Building("Monkey Temple Kathmandu", 2)
monkey_temple.purchase("Monkeys")
monkey_temple.construct()
monkey_temple.building_info()


