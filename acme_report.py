from random import randint, sample, uniform, random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
  """generating random products"""
  products = []
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

# collecting the list of 30 new random products into a variable
prod_list = generate_products()


def name_combine(prod_list):
  """breaking off names to combine them per instructions"""
  names_list = [item[0] for item in prod_list]
  return names_list
# saving my new list into a variable
prod_names = name_combine(prod_list)


def name_combine(prod_names):
  """writing a function to join the list, from a tuple to a string"""
  for i in range(len(prod_names)):
      names_list = print(''.join(prod_names[i][0]), ''.join(prod_names[i][1]))
      return names_list
# saving the final names list in a variable to call later
product_names_list = name_combine(prod_names)


# running a for loop to gather number of unique values
output = []
for x in prod_names:
    if x not in output:
        output.append(x)
# saving the number of unique values length as output
num_unique = len(output)


def avg_price(prod_list):
  """calculating average price from randomly generated list"""
  return [item[1] for item in prod_list]
# saving price average to call later
price_avg = sum(avg_price(prod_list)) / len(avg_price(prod_list))


def avg_weight(prod_list):
  """calculating average weight from randomly generated list"""
  return [item[2] for item in prod_list]
# saving weight average to call later
weight_avg = sum(avg_weight(prod_list)) / len(avg_weight(prod_list))


def avg_flamm(prod_list):
  """calculating average flammability from generate_products"""
  return [item[3] for item in prod_list]
# saving flammability average to call later
flamm_avg = sum(avg_flamm(prod_list)) / len(avg_flamm(prod_list))


# inventory report print out
def inventory_report(products):
  """Loop over the products to calculate the report."""
  print("ACME CORPORATION OFFICIAL INVENTORY REPORT",
  f'\nUnique product names: {num_unique}',
  f'\nAverage price: {price_avg}',
  f'\nAverage weight: {weight_avg}',
  f'\nAverage flammability: {flamm_avg}')


if __name__ == '__main__':
    inventory_report(generate_products())
