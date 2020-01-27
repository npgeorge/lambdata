from random import randint, sample, uniform, random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# generating random products
def generate_products(num_products=30):
    products = []
    # Generate and add random products.
    for x in range(num_products):
       nou = sample(NOUNS, k=1)
       adj = sample(ADJECTIVES, k=1)
       price = randint(5,100)
       weight = randint(5,100)
       flammability = uniform(0.0, 2.5)
       names = (adj,nou)
       description = (names,price,weight,flammability)  
       products.append(description)
    return products

def inventory_report(products):
    # Loop over the products to calculate the report.
    unique = unique(names)
    avg_price = sum(price)/len(products)
    avg_weight = sum(weight)/len(products)
    avg_flamm = sum(flammability)/len(products)
    for i in generate_products: 
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT",
    "Unique product names: ", unique,
    "Average price: ", avg_price,
    "Average weight: ", avg_weight,
    "Average flammability: ", avg_flamm) 


if __name__ == '__main__':
    inventory_report(generate_products())
```
"""