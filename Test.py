import unittest
from unittest.mock import MagicMock
from cartepizzeria import CartePizzeria
from cartepizzeriaexception import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty_true(self):
        self.assertTrue(self.carte.is_empty())

    def test_is_empty_false(self):
        pizza_mock = MagicMock()
        self.carte.add_pizza(pizza_mock)
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)

        pizza_mock = MagicMock()
        self.carte.add_pizza(pizza_mock)

        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_add_pizza(self):
        pizza_mock = MagicMock()
        self.carte.add_pizza(pizza_mock)

        self.assertIn(pizza_mock, self.carte.pizzas)

    def test_remove_pizza_success(self):
        pizza_mock = MagicMock()
        pizza_mock.name = "Margherita"

        self.carte.add_pizza(pizza_mock)
        self.carte.remove_pizza("Margherita")

        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_exception(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Inexistante")


if __name__ == "__main__":
    unittest.main()