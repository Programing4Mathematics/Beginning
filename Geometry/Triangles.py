>>> T = Triangle(P1, P2, P3)
>>> T.area                          # Note it gives a signed area
-11/2
>>> T.angles
{Point(0, 0): acos(2*sqrt(5)/25),
 Point(2, -1): acos(3*sqrt(130)/130),
 Point(3, 4): acos(23*sqrt(26)/130)}
>>> T.sides
[Segment(Point(0, 0), Point(3, 4)),
 Segment(Point(2, -1), Point(3, 4)),
 Segment(Point(0, 0), Point(2, -1))]
>>> T.perimeter
sqrt(5) + 5 + sqrt(26)
>>> T.is_right()                    # Is T a right triangle?
False
>>> T.is_equilateral()              # Is T equilateral?
False
>>> T.is_scalene()                  # Is T scalene?
True
>>> T.is_isosceles()                # Is T isosceles?
False

>>> T.altitudes
{Point(0, 0): Segment(Point(0, 0), Point(55/26, -11/26)),
 Point(2, -1): Segment(Point(6/25, 8/25), Point(2, -1)),
 Point(3, 4): Segment(Point(4/5, -2/5), Point(3, 4))}
>>> T.orthocenter                  # Intersection of the altitudes
Point(10/11, -2/11)
>>> T.bisectors()                  # Angle bisectors
{Point(0, 0): Segment(Point(0, 0), Point(sqrt(5)/4 + 7/4, -9/4 + 5*sqrt(5)/4)),
 Point(2, -1): Segment(Point(3*sqrt(5)/(sqrt(5) + sqrt(26)), 4*sqrt(5)/(sqrt(5) + sqrt(26))), Point(2, -1)),
 Point(3, 4): Segment(Point(-50 + 10*sqrt(26), -5*sqrt(26) + 25), Point(3, 4))}
>>> T.incenter                     # Intersection of angle bisectors
Point((3*sqrt(5) + 10)/(sqrt(5) + 5 + sqrt(26)), (-5 + 4*sqrt(5))/(sqrt(5) + 5 + sqrt(26)))
>>> T.incircle
Circle(Point((3*sqrt(5) + 10)/(sqrt(5) + 5 + sqrt(26)), (-5 + 4*sqrt(5))/(sqrt(5) + 5 + sqrt(26))), -11/(sqrt(5) + 5 + sqrt(26)))
>>> T.inradius
-11/(sqrt(5) + 5 + sqrt(26))
>>> T.medians
{Point(0, 0): Segment(Point(0, 0), Point(5/2, 3/2)),
 Point(2, -1): Segment(Point(3/2, 2), Point(2, -1)),
 Point(3, 4): Segment(Point(1, -1/2), Point(3, 4))}
>>> T.centroid                   # Intersection of the medians
Point(5/3, 1)
>>> T.circumcenter               # Intersection of perpendicular bisectors
Point(45/22, 35/22)
>>> T.circumcircle
Circle(Point(45/22, 35/22), 5*sqrt(130)/22)
>>> T.circumradius
5*sqrt(130)/22
>>> T.medial
Triangle(Point(3/2, 2), Point(5/2, 3/2), Point(1, -1/2))

>>> T.intersection(C1)
[Point(9/5, 12/5), Point(sqrt(113)/26 + 55/26, -11/26 + 5*sqrt(113)/26)]
>>> T.distance(T.circumcenter)
sqrt(26)/11
>>> T.is_similar(Triangle(P1, P2, P4))
False
