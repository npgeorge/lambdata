import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        wght = Product('Test Weight')
        self.assertEqual(prod.weight, 20)
    
    def test_stealability(self):
        steal = Product()
        self.assertGreater(prod.weight, 50)
    
    def test_explode(self):
        explo = Product()
        self.assertGreater(prod.flammability, 0.0)

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products), 30)
    

    def test_legal_names(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()