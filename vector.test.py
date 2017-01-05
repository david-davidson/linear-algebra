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

  def test_projection(self):
    v = Vector([-9.88,-3.264,-8.159])
    w = Vector([-2.155,-9.353,-9.473])
    projection_coords_rounded = v.get_projection(w).get_coords_rounded(3)
    self.assertEqual(projection_coords_rounded, [-1.530, -6.640, -6.725])

  def test_orthogonal_component(self):
    v = Vector([-9.88,-3.264,-8.159])
    w = Vector([-2.155,-9.353,-9.473])
    orthogonal_coords_rounded = v.get_orthogonal_component(w).get_coords_rounded(3)
    self.assertEqual(orthogonal_coords_rounded, [-8.350, 3.376, -1.434])

if __name__ == '__main__':
    unittest.main()
