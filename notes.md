#### Points vs. vectors
* Point: (2, 1) => x =2, y=1
* Vector represents *change*, e.g.:
[1,
 2]
  - Note different formatting: horizontal parens vs. vertical braces
  - Vectors not bound to any one point, are equal if the change they represent is equal
  - Represented with "overbar": v̅ (where bar is over text)

#### Operating on vectors
* Addition: if two vectors were placed end to end, where would they end up?
  Can simply add each individual coordinate
* Subtraction: v - w corresponds to the the vector from end of w to end of v, NOT from v to w. Corresponds to subtracting across each individual coordinate
* Scalar multiplication: "scales" a vector's length. Multiplies by each indiv. coordinate

#### Magnitude
* Length of a vector
* Via Pythag theorem, corresponds to sqrt x**2 + y**2. In n dimensions, model still applies: ||v|| (double bars: magnitude) = sqrt(x**2 + y**2 + ...)

#### Direction
* Unrelated to scale, so computed using "unit vector" of magnitude 1.
* Processing of finding unit vector: "normalizing". unit vector of v: "normalization" of v.
* (oh, and if all coords 0, it's the "0 vector", which indicates no change, has no direction)

#### Dot product
* Multiple two vectors * each other (each item * its counterpart), then sum the list. Represented by a dot.
* Not that useful on its own, but part of...

#### Inner product (angle between vectors)
* Angle between vectors, represented by theta (Θ)
* Note that any two vectors have *two* angles, the "long way" and the "short way" -- we always use the short way
* Represented by arc cosine of (dot product of two vectors) / (magnitudes of both vectors, multiplied)
