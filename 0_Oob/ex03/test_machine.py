import unittest
import random
from machine import *

class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        """Set up a new coffee machine and a list of beverages for each test."""
        self.coffee_machine = CoffeeMachine()
        self.beverages = [Coffee, Tea, Chocolate, Cappuccino]

    def test_serve_until_breakdown(self):
        """Test that the coffee machine serves exactly 10 drinks before breaking down."""
        try:
            for _ in range(10):
                beverage_class = random.choice(self.beverages)
                drink = self.coffee_machine.serve(beverage_class)
                # Checking if the beverage is not an empty cup, since an empty cup is a valid output randomly
                if isinstance(drink, EmptyCup):
                    print("Served an Empty Cup.")
                else:
                    print(f"Served: {drink}")
        except BrokenMachineException:
            self.fail("The machine should not break down before serving 10 drinks.")

        # The 11th serve should raise a BrokenMachineException
        with self.assertRaises(BrokenMachineException, msg="The machine should break down on the 11th serve."):
            self.coffee_machine.serve(random.choice(self.beverages))

    def test_repair_functionality(self):
        """Test that the machine can be repaired after breaking and then serve more drinks."""
        # Breaking the machine first
        for _ in range(10):
            self.coffee_machine.serve(random.choice(self.beverages))

        with self.assertRaises(BrokenMachineException):
            self.coffee_machine.serve(random.choice(self.beverages))

        # Repair the machine
        self.coffee_machine.repair()

        # Test if machine serves after repair without breaking immediately
        try:
            for _ in range(10):
                beverage_class = random.choice(self.beverages)
                drink = self.coffee_machine.serve(beverage_class)
                if isinstance(drink, EmptyCup):
                    print("Served an Empty Cup after repair.")
                else:
                    print(f"Served after repair: {drink}")
        except BrokenMachineException:
            self.fail("The machine should not break down immediately after repair.")

        # Should break again after the next 10 serves
        with self.assertRaises(BrokenMachineException, msg="The machine should break down again after another 10 serves."):
            self.coffee_machine.serve(random.choice(self.beverages))

if __name__ == "__main__":
    unittest.main()

