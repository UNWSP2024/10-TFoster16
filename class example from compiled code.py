#Timothy Foster, 3/26/25, Program #1

#Car class
class Car:
    def __init__ (self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

#Example code to show how class works is written below.

truck = Car("Ford", "F150", "2016")

if __name__ == "__main__":
    txt = truck.get_make()
    print(txt)
