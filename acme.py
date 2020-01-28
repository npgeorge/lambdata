# importing random
import random

# defining the class attributes
class Product:
    """
    Product class - defines the attributes of an acme product.
    """
    def __init__(self, name, identifier=random.randint(1000000, 9999999), price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
   

    def stealability(self):
        """Stealability function and outputs."""
        stealable = (self.price/self.weight)
        if stealable < 0.5:
            print("Not so stealable...")
        elif stealable >= 0.5 and stealable < 1.0:
            print("Kinda stealable.")
        else:
            print("Very stealable!")
   

    def explode(self):
        """Explosion function and output"""
        explosion = self.flammability*self.weight
        if explosion < 10:
            print("...fizzle.")
        elif explosion >= 10 or explosion < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):
    """
    An example of a Boxing Glove as a product, inheriting the Product class.
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        super().__init__(name, weight=10)


    def explode(self):
        print("...it's a glove.")
    

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif self.weight >= 5 and self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
