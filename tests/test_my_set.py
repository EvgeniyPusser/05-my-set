import unittest

from my_set.my_set import MySet


class CollidingValue:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, CollidingValue) and self.value == other.value


class TestMySet(unittest.TestCase):
    def test_new_set_is_empty(self):
        values = MySet()

        self.assertEqual(len(values), 0)
        self.assertEqual(list(values), [])

    def test_add_returns_true_for_new_element_and_false_for_duplicate(self):
        values = MySet()

        self.assertTrue(values.add("item"))
        self.assertFalse(values.add("item"))
        self.assertEqual(len(values), 1)
        self.assertIn("item", values)


    def test_remove_returns_true_for_existing_element_and_false_for_missing(self):
        values = MySet()
        values.add("item")

        self.assertTrue(values.remove("item"))
        self.assertFalse(values.remove("item"))
        self.assertEqual(len(values), 0)
        self.assertNotIn("item", values)


    def test_colliding_elements_are_stored_and_removed_independently(self):
        first = CollidingValue("first")
        second = CollidingValue("second")
        values = MySet(capacity=2)

        self.assertTrue(values.add(first))
        self.assertTrue(values.add(second))
        self.assertIn(first, values)
        self.assertIn(second, values)
        self.assertEqual(len(values), 2)

        self.assertTrue(values.remove(first))
        self.assertNotIn(first, values)
        self.assertIn(second, values)
        self.assertEqual(len(values), 1)


    def test_add_resizes_and_preserves_all_elements(self):
        values = MySet(capacity=4, load_factor=0.75)
        expected = set(range(4))

        for element in expected:
            self.assertTrue(values.add(element))

        self.assertEqual(values.capacity, 8)
        self.assertEqual(set(values), expected)
        self.assertEqual(len(values), len(expected))


    def test_iteration_returns_each_element_once(self):
        values = MySet()
        expected = {"one", "two", "three"}

        for element in expected:
            values.add(element)

        self.assertEqual(set(values), expected)
        self.assertEqual(len(list(values)), len(expected))
