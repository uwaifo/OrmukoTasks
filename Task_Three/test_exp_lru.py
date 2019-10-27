import unittest
import exp_lru

class TestExpiringLru(unittest.TestCase):

    def init(self):
        self.tester = exp_lru.ExpiringCache()
    
    def test_one(self):
        mocker = [1]
        #self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.tester.push_cache(1), exp_lru.PUSHED_CACHE_OBJ)



if __name__ == '__main__':
    unittest.main()