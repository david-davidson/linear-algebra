import unittest
from vector import Vector

class TestVectorMethods(unittest.TestCase):

  def test_addition(self): # methods must start with `test` to run
    v = Vector([1,2])
    w = Vector([3,4])
    self.assertEqual(v + w, Vector([4,6]))

  def test_subtraction(self):
    v = Vector([1,2])
    w = Vector([3,4])
    self.assertEqual(v - w, Vector([-2,-2]))

  def test_scalar_multiplication(self):
    v = Vector([1,2])
    scale = 10
    self.assertEqual(v.get_scalar_multiply(10), Vector([10, 20]))

  def test_magnitude(self):
    v = Vector([3,4])
    self.assertEqual(v.get_magnitude(), 5)

  def test_direction(self):
    v = Vector([1,2])
    unit_vector = v.get_direction()
    self.assertEqual(unit_vector.get_coords_rounded(3), [0.447, 0.894])

  def test_dot_product(self):
    v = Vector([1,2])
    w = Vector([3,4])
    self.assertEqual(v.get_dot_product(w), 11)

  def test_inner_product(self):
    v = Vector([0,1])
    w = Vector([1,0])
    inner_product = v.get_inner_product(w)
    self.assertEqual(inner_product["degrees"], 90)
    self.assertEqual(round(inner_product["radians"], 3), 1.571)

  def test_parallel(self):
    v = Vector([1,2])
    w = Vector([-2,-4])
    x = Vector([1,3])
    self.assertTrue(v.is_parallel_with(w))
    self.assertFalse(v.is_parallel_with(x))

  def test_orthogonal(self):
    v = Vector([1,2])
    w = Vector([-2,1])
    x = Vector([1,3])
    self.assertTrue(v.is_orthogonal_to(w))
    self.assertFalse(v.is_orthogonal_to(x))

if __name__ == '__main__':
    unittest.main()
