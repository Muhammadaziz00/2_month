# # ИИНКАПСУЛЯЦИЯ
# class Smartphon:
#     def __init__(self, model, sim_cards, battery):
#         self.model = model # публичный
#         self.__sim_cards = sim_cards
#         self._battery = battery

#     @property
#     def sim_cards(self):
#         return self.__sim_cards




#     def info(self): # публичный метот, отрибут 
#         print(f"модель  - {self.model},  сим карта - {self.__sim_cards}, батарея - {self._battery}")
#         self._gallery()
#         # self.__password()



#     def _gallery(self):
#         print(" фотографии или галерея")
        


#     def __password(self):
#         print("12345678")

#     @property
#     def password(self):
#         return self.__password

        
# mi = Smartphon("note 10", ["mega", "O!"], "5000 Mach")
# # mi.info()
# print(mi.model)
# print(mi._battery)
# print(mi.sim_cards)
# # mi.password()
# mi.password()




def private(func):
    def test():
        print(" hello world")
        func()
        print("bye!")

    return test 

@private
def hello():
    print("WTF!!!!!
          ")

hello()
