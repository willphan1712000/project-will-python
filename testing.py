import unittest
from willphanpy import Wpya as a
from willphanpy import Wpyd as d

# class inheritance in python
class SortTesting(unittest.TestCase):
    def test1(self):
        arr = d.randomInt(1,50, shuffle=True)
        a.sort(arr, algorithm='merge')
        correct = d.randomInt(1,50)
        self.assertEqual(arr, correct)
    def test2(self):
        arr = d.randomInt(1,50, shuffle=True)
        a.sort(arr, algorithm='merge')
        correct = d.randomInt(1,50)
        self.assertEqual(arr, correct)
    def test3(self):
        arr = d.randomInt(1,50, shuffle=True)
        a.sort(arr, algorithm='merge')
        correct = d.randomInt(1,50)
        self.assertEqual(arr, correct)
    def test4(self):
        arr = d.randomInt(1,50, shuffle=True)
        a.sort(arr, algorithm='merge')
        correct = d.randomInt(1,50)
        self.assertEqual(arr, correct)
    def test5(self):
        arr = d.randomInt(1,50, shuffle=True)
        a.sort(arr, algorithm='merge')
        correct = d.randomInt(1,50)
        self.assertEqual(arr, correct)

if __name__ == '__main__':
    unittest.main()