>>> from sympy.geometry import *
>>> P1 = Point(0, 0)
>>> P2 = Point(3, 4)
>>> P3 = Point(2, -1)
>>> P4 = Point(-1, 5)
>>> S1 = Segment(P1, P2)
>>> S2 = Segment(P3, P4)
>>> Point.is_collinear(P1, P2, P3)
False
>>> S1.length
5
>>> S2.midpoint
Point(1/2, 2)
>>> S1.slope
4/3
>>> S1.intersection(S2)
[Point(9/10, 6/5)]
>>> Segment.angle_between(S1, S2)
acos(-sqrt(5)/5)
>>> S1.contains(P3)
False
