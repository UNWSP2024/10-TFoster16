#Timothy Foster, 3/26/35, Car Class Program

#Define the Car class.
class Car:

    #Initialize the class with the year_model, make, and speed data attributes.
    def __init__ (self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    #Define the sets for the class.

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    #Define the accelerate and brake methods.
    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    #Define the gets for the class.

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

#Define the function.
def speed_up_and_brake():
    #Define an object of the class.
    vehicle = Car("2015 Soul", "Kia", 0)

    #Use a for loop to call the accelerate method, get the speed, and print the results five times.
    for counter in range(5):
        vehicle.accelerate()
        current_speed = vehicle.get_speed()
        print(current_speed)

    #Use a for loop to call the brake method, get the speed, and print the results five times.
    for counter in range(5):
        vehicle.brake()
        current_speed = vehicle.get_speed()
        print(current_speed)

#Call the above function.
if __name__ == "__main__":
    speed_up_and_brake()




