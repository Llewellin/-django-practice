from django.test import TestCase

from app.calc import add
from app.calc import subtract

class CalcTest (TestCase):
    def test_add_number(self):
        """Test that add number are added together"""
        self.assertEqual(add(3,8), 11)
    def test_subtract_number(self):
        """Test substraction"""
        self.assertEqual(subtract(8,3), 5)
