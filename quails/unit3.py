import inspect
import re
import unittest
import math

# Define class 'Circle' and its methods:
class Circle:

    def __init__(self, radius):
        self.radius = 0
        if not isinstance(radius,(float,int)):
            raise ValueError('radius must be a number')
        elif(radius<0 or radius>1000):
            raise ValueError('radius must be between 0 and inclusive')
        else:
            self.radius=radius


    def area(self):
        return round(math.pi*(self.radius**2),2)

    def circumference(self):
        return round(math.pi*self.radius*2,2)

class TestCircleCircumference(unittest.TestCase):

    def test_circlecircum_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(), 15.71)


    def test_circlecircum_with_min_radius(self):
        c2 = Circle(0)
        self.assertEqual(c2.circumference(),0)



    def test_circlecircum_with_max_radius(self):
        c3 = Circle(1000)
        self.assertEqual(c3.circumference(),6283.19)


if __name__ == '__main__':
