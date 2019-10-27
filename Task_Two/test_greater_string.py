import  unittest
import greater_string

class TestGreater(unittest.TestCase):
    def test_greater_string(self):
        
        self.assertEqual(greater_string.greaterString('1.2','1.1'),1.2)
        self.assertEqual(greater_string.greaterString('2.1','2.11'), 2.11)
    
    def test_valid_string(self): 
        error_1 = "Invalid entry: One or both of your string arguments has no numeric values"
        self.assertEqual(greater_string.greaterString("2.1", "two"), error_1 )
        self.assertEqual(greater_string.greaterString("one point two", "one pont one"), error_1)
    
    def test_valid_arg(self):
        error_2 = "Invalid entry: One or both of your string arguments has multiple numeric values"
        self.assertEqual(greater_string.greaterString("3.2", "7 9 0"),error_2)
        self.assertEqual(greater_string.greaterString('1.2 4','2.11'),error_2)

if __name__ == "__main__":
        unittest.main()

 