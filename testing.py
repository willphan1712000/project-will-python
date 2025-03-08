import unittest

from Wp import Wp
# class inheritance in python
class TestWp1(unittest.TestCase):
    def test_postfix1(self):
        self.assertEqual(Wp.infixToPostfix("a*(b+c)-d/e"), "abc+*de/-")
    def test_postfix2(self):
        self.assertEqual(Wp.infixToPostfix("(a-b)*c"), "ab-c*")

    def test_evaluation1(self):
        self.assertEqual(Wp.evaluatePostfix(Wp.infixToPostfix("(2+3)*5")), 25)
    def test_evaluation2(self):
        self.assertEqual(Wp.evaluatePostfix(Wp.infixToPostfix("2+(3+1)*2")), 10)
    def test_evaluation3(self):
        self.assertEqual(Wp.evaluatePostfix(Wp.infixToPostfix("2+(1+4)+6/3")), 9)

if __name__ == '__main__':
    unittest.main()