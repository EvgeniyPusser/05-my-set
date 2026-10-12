import unittest

from my_stack import MyStackInt


class TestMyStackInt(unittest.TestCase):

    def test_push_and_max(self):
        stack = MyStackInt()

        stack.push(3)
        self.assertEqual(stack.max(), 3)

        stack.push(7)
        self.assertEqual(stack.max(), 7)

        stack.push(2)
        self.assertEqual(stack.max(), 7)

    def test_pop(self):
        stack = MyStackInt()

        stack.push(3)
        stack.push(7)
        stack.push(2)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.max(), 7)

        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.max(), 3)

    def test_pop_empty(self):
        stack = MyStackInt()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_max_empty(self):
        stack = MyStackInt()

        with self.assertRaises(IndexError):
            stack.max()


if __name__ == "__main__":
    unittest.main()