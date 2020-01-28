import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, prod_list, product_names_list, name_combine


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Weight')
        self.assertEqual(prod.weight, 20)
    

    def test_stealability(self):
        """Tests if stealability function is working"""
        prod = Product('Test Stealability')
        self.assertNotEqual(prod.stealability, 2)
    

    def test_explode(self):
        """Tests for a large explosion"""
        prod = Product('Test Explode')
        self.assertNotEqual(prod.explode, 60)


class AcmeReportTests(unittest.TestCase):
    """
    creating new acme report
    """

    def test_default_num_products(self):
        """checking the length of the generate products function"""
        report = generate_products('Test Generate Products Length')
        # imported prod_list variable for ease of use
        self.assertEqual(len(prod_names), 30)
    
    # checking the legal name, Adjective IN product_names_list, space, and NOUNS
    def test_legal_names(self):
        """checking the legal name, Adjective IN product_names_list, space, and NOUNS"""
        report = Product('Test Legal Names')
        self.assertIn(ADJECTIVES, product_names_list)
        self.assertIn(" ", product_names_list)
        self.assertIn(NOUNS, product_names_list)


if __name__ == '__main__':
    unittest.main()
    
