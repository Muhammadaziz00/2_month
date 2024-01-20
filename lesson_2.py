class Animal:
    def __init__(self,breed,classes,year, color):
        self.breed = breed
        self.year = year
        self.color = color
        self.clases = classes 

        # def info(self):
        #     print(f"{self.breed}, {self.classes}, {self.year}, {self.color}, {self.age}")


# class Dog (Animal) :
#     def __init__(self, breed, classes, color, age):
#         super().__init__(breed, classes, color, age)
#         self.paws = 4

#     def info(self):
#         print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во лап -{}")




class Snake(Animal):
    pass

anakonda = Snake("anakonda", "Чешуйчитая", "Розовый", 16)
print(f"{anakonda.breed}, {anakonda.classes}, {anakonda.color}, {anakonda.age}")