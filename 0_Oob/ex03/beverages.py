class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup."

    def __str__(self): 
        return (f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.price = 0.40
        self.name = "coffee"

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.price = 0.50
        self.name = "chocolate"

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.price = 0.45
        self.name = "cappuccino"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"
        
# Testing the classes
if __name__ == "__main__":
    basic_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(basic_beverage)
    print()
    print(coffee)
    print()
    print(tea)
    print()
    print(chocolate)
    print()
    print(cappuccino)
