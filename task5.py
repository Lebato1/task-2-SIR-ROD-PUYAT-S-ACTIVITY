class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary  

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"{self.name} received a raise of ₱{amount}.")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ₱{self.__salary}")

emp = Employee("ramil lebato", "Manager", 85000)
emp.display_employee()
emp.give_raise(7000)
emp.display_employee()
