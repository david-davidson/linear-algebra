import unittest
from vector import Vector

class TestVectorMethods(unittest.TestCase):

  def test_addition(self): # methods must start with `test` to run
    """
    Adds two Vectors: returns a new Vector formed by adding each item to its counterpart.
    """
    vector1 = Vector([1,2])
    vector2 = Vector([3,4])
    self.assertEqual(vector1 + vector2, Vector([4,6]))

  def test_subtraction(self):
    """
    Subtracts one Vector from another: returns a new one formed by subtracting each item from its
    counterpart.
    """
    vector1 = Vector([1,2])
    vector2 = Vector([3,4])
    self.assertEqual(vector1 - vector2, Vector([-2,-2]))

  def test_scalar_multiplication(self):
    """
    Accepts a number and returns a new Vector formed by multiplying it by each item.
    """
    vector = Vector([1,2])
    scale = 10
    self.assertEqual(vector.get_scalar_multiply(10), Vector([10, 20]))

  def test_magnitude(self):
    """
    Returns a Vector's length (magnitude).
    """
    vector = Vector([3,4])
    self.assertEqual(vector.get_magnitude(), 5)

  def test_direction(self):
    """
    Returns a Vector equivalent to the original but of magnitude 1: that is, the 'unit vector'.
    """
    vector = Vector([1,2])
    unit_vector = vector.get_direction()
    self.assertEqual(unit_vector.get_coords_rounded(3), [0.447, 0.894])

  def test_dot_product(self):
    """
    Returns the 'dot product' of two Vectors: each item multiplied by its counterpart, then list
    summed.
    """
    vector1 = Vector([1,2])
    vector2 = Vector([3,4])
    self.assertEqual(vector1.get_dot_product(vector2), 11)

  def test_inner_product(self):
    """
    Returns, in both degrees and radians, the 'inner product' (angle between) two Vectors.
    """
    vector1 = Vector([0,1])
    vector2 = Vector([1,0])
    inner_product = vector1.get_inner_product(vector2)
    self.assertEqual(inner_product["degrees"], 90)
    self.assertEqual(round(inner_product["radians"], 3), 1.571)

if __name__ == '__main__':
    unittest.main()
