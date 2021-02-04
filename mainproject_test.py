import mainproject
import unittest
from io import StringIO
print('We will be using Fizzy drinks to test our code')




class Testmainproject(unittest.TestCase):
    def test_drink_list(self): 
        current_products = ["Fanta", "Coke", "Sprite", "Lemonade"]
        expected = current_products
        actual = mainproject.get_items(current_products)
        self.assertEqual(expected,actual)



        assert expected == actual
    
   

if __name__=='__main__':
    unittest.main()