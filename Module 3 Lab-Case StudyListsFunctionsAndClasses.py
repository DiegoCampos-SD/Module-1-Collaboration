'''
Author: Diego Campos
File name: Module 3 Lab - Case Study: Lists, Functions, and Classes
Description:    This application asks the user for the year, make,
                model, number of doors and roof type; processes the
                data and prints the information entered by the user
                and also the type of vehicle (car by default).
'''

#Super class
class Vehicle():
    
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
        
#Depending class of Super class
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
#Function to display all the information
    def displayInfo(self):
        print(f"Vehicle type: {self.vehicleType}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
        
#Function that interact with the user and also verify the input for number of doors and type of roof
def createAutomobile():   
    print("Please enter the details for your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    

    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        else:
            print("Please enter a valid number of doors (2 or 4).")
    

    while True:
        roof = input("Type of roof (solid or sun roof): ").lower()
        if roof in ['solid', 'sun roof']:
            break
        else:
            print("Please enter a valid roof type (solid or sun roof).")
    

    car = Automobile(year, make, model, doors, roof)
    

    car.displayInfo()


def main():
    createAutomobile()
    

if __name__ == "__main__":
    main()