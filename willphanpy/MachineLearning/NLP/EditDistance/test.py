import unittest
from algo import editDistance

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(editDistance('', ''), 0)
    def test2(self):
        self.assertEqual(editDistance('abc', ''), 3)
    def test3(self):
        self.assertEqual(editDistance('kitten', 'sitting'), 3)
    def test4(self):
        self.assertEqual(editDistance('intention', 'execution'), 5)
    def test5(self):
        self.assertEqual(editDistance('flaw', 'lawn'), 2)
    def test6(self):
        self.assertEqual(editDistance('s', 'strhgti'), 6)
    def test7(self):
        self.assertEqual(editDistance('nhaphan', 'willphan'), 4)
    def test8(self):
        self.assertEqual(editDistance('sunday', 'saturday'), 3)
    def test9(self):
        self.assertEqual(editDistance('intention', 'execution'), 5)
    def test10(self):
        self.assertEqual(editDistance('executive', 'execution'), 2)

if __name__ == '__main__':
    unittest.main()