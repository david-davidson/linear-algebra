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
    return Vector(self._merge_with_transformation(other, lambda x, y: x + y))

  # Implicitly called in `-` operations
  def __sub__(self, other):
    return Vector(self._merge_with_transformation(other, lambda x, y: x - y))

  # Implicitly called in `*` operations
  def __mul__(self, scale):
    return Vector([item * scale for item in self.coords])

  # Merges two lists and applies `transform` to each item pair
  def _merge_with_transformation(self, other, transform):
    return [transform(x, y) for x, y
      # ^ list comprehension iterates over list, like `map`
      in zip(self.coords, other.coords)]
      # ^ `zip` merges equal-length lists into list of pairs

  # Returns length of vector
  def magnitude(self):
    return math.sqrt(sum([x**2 for x in self.coords]))

  # Returns direction of vector
  def get_direction(self):
    return self * (1 / self.magnitude())

  # Returns "dot product" of two vectors: each item multiplied by counterpart, then list summed
  def dot_product(self, other):
    items_multiplied = self._merge_with_transformation(other, lambda x, y: x * y)
    return sum(items_multiplied)
