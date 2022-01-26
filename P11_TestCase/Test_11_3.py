import Employee as E
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = E.Employee('Le Hoang', 'Vu', 4900)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.year_salary, 9900)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(100)
        self.assertEqual(self.my_employee.year_salary, 5000)

if __name__ == '__main__':
    unittest.main()
