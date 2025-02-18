class Car:
 
    def __init__(self, brand_name, model_name, year_manufactured):
     
        self.brand = brand_name  
        self.model = model_name  
        self.year = year_manufactured  

        print(f"A new Car object has been created: Brand - {self.brand}, Model - {self.model}, Year - {self.year}")

    def display_info(self):
       
        print("----- Car Information -----")  
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print("-------------------------") 

car1 = Car("Ford", "Mustang", 1967)  
car2 = Car("Tesla", "Model S", 2024) 

print("\nDetails for Car 1:")
car1.display_info()

print("\nDetails for Car 2:")
car2.display_info()