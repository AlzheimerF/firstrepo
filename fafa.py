# def my_func(f, s):
#     f = str(f)
#     s = str(s)
#     identity = 0
#     undex_ = 0
#     for x in f:
#         if x == s[undex_]:
#             identity += 10
#             undex_ += 1
#
#     return f"{identity} %"
#
# a = ["123124", "1fsafdsf"]
# print(my_func("123Gav", "Gavfafa"))

class Birds:
    def __init__(self, colour, type1, place_of_residence):
        self.colour = colour
        self.type = type1
        self.place_of_residence = place_of_residence
        self.type_ = "Birds"

    def info(self):
        print(f"""Информация о {self.type}
              Цвет: {self.colour}
              Место обитания: {self.place_of_residence}""")


class Fish:
    def __init__(self, count_fins, type1, place_of_residence):
        self.count_fins = count_fins
        self.type = type1
        self.place_of_residence = place_of_residence
        self.type_ = "Fish"
    def info(self):
        print(f"""Информация о {self.type}
              Количество плавников: {self.count_fins}
              Место обитания: {self.place_of_residence}""")


class Mammals:
    def __init__(self, colour, type1, place_of_residence):
        self.colour = colour
        self.type = type1
        self.place_of_residence = place_of_residence
        self.type_ = "Mammals"

    def info(self):
        print(f"""Информация о {self.type}
              Цвет: {self.colour}
              Место обитания: {self.place_of_residence}""")


class Predators:
    def __init__(self):
        self.type_1 = "Predators"
        self.favourite_food = "Мяско"

    def eat(self):
        print(f"Животное питается: {self.favourite_food}")


class Herbivores:
    def __init__(self):
        self.type_1 = "Herbivores"
        self.favourite_food = "Травка"

    def eat(self):
        print(f"Животное питается: {self.favourite_food}")


class Falcon(Birds, Predators):
    def __init__(self, colour, type1, place_of_residence):
        Birds.__init__(self, colour, type1, place_of_residence)
        Predators.__init__(self)
    def info(self):
        print(f"""Информация о {self.type}:
              Тип: {self.type_1}
              ПодТип: {self.type_} 
              Цвет: {self.colour}
              Место обитания: {self.place_of_residence}""")
        Predators.eat(self)


class Penguin(Birds, Predators):
    def __init__(self, colour, type1, place_of_residence):
        Birds.__init__(self, colour, type1, place_of_residence)
        Predators.__init__(self)

    def info(self):
        print(f"""Информация о {self.type}:
                 Тип: {self.type_1}
                 ПодТип: {self.type_} 
                 Цвет: {self.colour}
                 Место обитания: {self.place_of_residence}""")
        Predators.eat(self)


class Trout(Fish, Predators):
    def __init__(self, count_fins, type1, place_of_residence):
        Fish.__init__(self, count_fins, type1, place_of_residence)
        Predators.__init__(self)

    def info(self):
        print(f"""Информация о {self.type}:
                 Тип: {self.type_1}
                 ПодТип: {self.type_} 
                 Количество плавников: {self.count_fins}
                 Место обитания: {self.place_of_residence}""")
        Predators.eat(self)


class Whale(Mammals, Predators):
    def __init__(self, count_fins, colour, type1, place_of_residence):
        Mammals.__init__(self, colour, type1, place_of_residence)
        self.count_fins = count_fins
        Predators.__init__(self)

    def info(self):
        print(f"""Информация о {self.type}:
                 Тип: {self.type_1}
                 ПодТип: {self.type_} 
                 Цвет: {self.colour}
                 Количество плавников: {self.count_fins}
                 Место обитания: {self.place_of_residence}""")
        Predators.eat(self)

falcon = Falcon("Черный", "Falcon", "Америка - да, пример дибильный...")
falcon.info()

print("----------------------------")

penguin = Penguin("Черно-белый", "Penguin", "Антарктида - да, пример дибильный...")
penguin.info()

print("----------------------------")

trout = Trout(4, "Trout", "Озера - да, пример дибильный...")
trout.info()

print("----------------------------")

whale = Whale(5, "Синий", "Whale", "Море - да, пример дибильный...")
whale.info()