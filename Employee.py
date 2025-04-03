#Timothy Foster, 3/26/25, Employee Class Program

#Define the class.
class Employee:

    #Initialize the class.
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    #Define the sets.
    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    #Define the gets.
    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

#Define the function.
def create_and_print_employee_data():

    #Make new objects with the Employee class.
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    #Call data from the each class and assign it to the variable.
    employee1_info = "Employee 1: " + f"{employee1.get_name()}, " + f"{employee1.get_ID_number()}, " + f"{employee1.get_department()}, " + f"{employee1.get_job_title()}"
    employee2_info = "Employee 2: " + f"{employee2.get_name()}, " + f"{employee2.get_ID_number()}, " + f"{employee2.get_department()}, " + f"{employee2.get_job_title()}"
    employee3_info = "Employee 3: " + f"{employee3.get_name()}, " + f"{employee3.get_ID_number()}, " + f"{employee3.get_department()}, " + f"{employee3.get_job_title()}"

    #Print the results.
    print(employee1_info)
    print(employee2_info)
    print(employee3_info)

if __name__ == "__main__":
    create_and_print_employee_data()
