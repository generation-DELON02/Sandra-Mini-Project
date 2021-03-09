
import mini_project_db  
import unittest      
from io import StringIO
from _pytest.monkeypatch import MonkeyPatch 
def print_heading_in_colour_font():
    class color:
        PURPLE = '\033[95m'
        GREEN = '\033[92m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    print(color.PURPLE + color.UNDERLINE + color.BOLD + "***Sandra's Mini Project Test ***\n"+ color.END)
    print(color.GREEN +'---We will be using non-alcoholic drinks to test our code---' + color.END)
print_heading_in_colour_font()
#to do list 
class miniprojtest(unittest.TestCase):
    def setUp(self):
        self.monkeypatch = MonkeyPatch() # defined a class variable called monkey patch 
    def test_new_drink_name_input(self):
        #call function and assert what you think it is
        new_drink_name_input = "Vimto"
        def mock_input(a): #created a mock function to create a pretend input
            return new_drink_name_input
        self.monkeypatch.setattr("builtins.input",mock_input) #mock a module called builtins.input 
        result = mini_project_db.new_drink_name_input() #from your actual project file
        assert result == "Vimto"
            
        
    
if __name__=='__main__':
    unittest.main()