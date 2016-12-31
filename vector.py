import math

class Vector(object):
  def __init__(self, coords):
    self.coords = tuple(coords)

  # Implicitly called in `print` statements
  def __str__(self):
    return "Coordinates: {}".format(self.coords)

  # Implicitly called in `==` comparisons
  def __eq__(self, other):
    return self.coords == other.coords

  # Implicitly called in `+` operations
  def __add__(self, other):
    return self._merge_with_transformation(other, lambda x, y: x + y)

  # Implicitly called in `-` operations
  def __sub__(self, other):
    return self._merge_with_transformation(other, lambda x, y: x - y)

  # Implicitly called in `*` operations
  def __mul__(self, scale):
    return Vector([item * scale for item in self.coords])

  def _merge_with_transformation(self, other, transform):
    return Vector([transform(x, y) for x, y
      # ^ list comprehension iterates over list, like `map`
      in zip(self.coords, other.coords)])
      # ^ `zip` merges equal-length lists into list of pairs

  def get_magnitude(self):
    return math.sqrt(sum([x**2 for x in self.coords]))

  def get_direction(self):
    return self * (1 / self.get_magnitude())
