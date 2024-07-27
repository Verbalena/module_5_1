class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor

        if 1 <= self.new_floor <= self.number_of_floors:
            for i in range(self.new_floor):
                print(i+1)
        elif self.new_floor <= 1 or self.new_floor >= self.number_of_floors:
            print('Такого этажа не существует')

house_1 = House('ЖК Горский', 18)
house_2 = House('Домик в деревне', 2)

house_1.go_to(5)
house_2.go_to(10)


