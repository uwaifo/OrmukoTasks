import unittest
import if_overlaping


class TestOverlap(unittest.TestCase):
    
    def test_if_overlapping(self):
        self.assertAlmostEqual(if_overlaping.ifOverlaping(1,5,2,6), "Overlaping")
        self.assertAlmostEqual(if_overlaping.ifOverlaping(1,5,6,8), "Overlaping")

    if __name__ == "__main__":
        unittest.main()