import math

class Vector(object):

  def __init__(self, coords):
    self.coords = tuple(coords)

  def __str__(self):
    return "Coordinates: {}".format(self.coords)

  def __eq__(self, other):
    return self.coords == other.coords

  def __add__(self, other):
    """
    Adds two Vectors.

    Returns a new Vector formed by adding each item to its counterpart. Implicitly called in `+`
    operations.
    """
    return Vector(self._merge_with_transformation(other, lambda x, y: x + y))

  def __sub__(self, other):
    """
    Subtracts one Vector from another.

    Returns a new Vector formed by subtracting each item from its
    counterpart. Implicitly called in `-` operations.
    """
    return Vector(self._merge_with_transformation(other, lambda x, y: x - y))

  def _merge_with_transformation(self, other, transform):
    """Merges two lists and applies `transform` to each item pair."""
    return [transform(x, y) for x, y  # ^ list comprehension iterates over list, like `map`
      in zip(self.coords, other.coords)]  # ^ `zip` merges equal-length lists into list of pairs

  def get_coords_rounded(self, decimal_places):
    """Returns coords rounded to requested decimal place."""
    return [round(x, decimal_places) for x in self.coords]

  def get_scalar_multiply(self, scale):
    """Accepts a number and returns a new Vector formed by multiplying it by each item."""
    return Vector([item * scale for item in self.coords])

  def get_magnitude(self):
    """Returns a Vector's length (magnitude)."""
    return math.sqrt(sum([x**2 for x in self.coords]))

  def get_direction(self):
    """
    Returns a Vector's direction.

    This is expressed as a Vector equivalent to the original but of magnitude 1: that is, the
    'unit vector'.
    """
    return self.get_scalar_multiply(1 / self.get_magnitude())

  def get_dot_product(self, other):
    """
    Returns the 'dot product' of two Vectors.

    This is the result of multiplying each item by its counterpart, then summing the list.
    """
    items_multiplied = self._merge_with_transformation(other, lambda x, y: x * y)
    return sum(items_multiplied)

  def get_inner_product(self, other):
    """Returns, in both degrees and radians, the 'inner product' (angle between) two Vectors."""
    dot_product = self.get_dot_product(other)
    magnitudes_multiplied = self.get_magnitude() * other.get_magnitude()
    inner_product_radians = math.acos(dot_product / magnitudes_multiplied)
    return {
      "radians": inner_product_radians,
      "degrees": math.degrees(inner_product_radians)
    }
