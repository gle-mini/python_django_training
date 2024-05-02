import random
from beverages import *

class EmptyCup(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "empty cup"
        self.price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"

class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")



class CoffeeMachine:
    def __init__(self):
        self.count = 0
        self.is_broken = False

    def repair(self):
        self.is_broken = False
        self.count = 0

    def serve(self, hot_beverage):
        if self.is_broken:
            raise BrokenMachineException()
        if self.count >= 10:
            self.is_broken = True
            raise BrokenMachineException()

        self.count += 1
        if random.choice([True, False]):
            return hot_beverage()
        else:
            return EmptyCup()
        

# Example usage
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]  # List of beverage classes

    try:
        for _ in range(15):  # Attempt to serve 15 times to force an error after 10
            selected_beverage = random.choice(beverages)
            drink = coffee_machine.serve(selected_beverage)
            print(drink)
    except BrokenMachineException as e:
        print(e)
        coffee_machine.repair()
        print("Machine repaired!")

        # Try serving again after repair
        try:
            for _ in range(15):
                selected_beverage = random.choice(beverages)
                drink = coffee_machine.serve(selected_beverage)
                print(drink)
        except BrokenMachineException as e:
            print(e)
            print("The machine broke down again!")
