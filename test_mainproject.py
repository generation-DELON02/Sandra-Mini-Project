import mainproject as main 
import unittest
from io import StringIO
print('We will be using the real drinks to test our code')


class Testmainproject(unittest.TestCase):
    def test_drink_list(self): 
         current_products = ["Beer", "Vodka", "Wine", "Rose", "Prosecco", "coke"]
         expected = current_products
         actual = main.get_drinks_list(current_products)
         print(self.assertEqual(expected,actual))
        
    
   

if __name__=='__main__':
    unittest.main()