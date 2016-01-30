>>> C1 = Circle(P1, 3)
>>> C2 = Circle(P2, P3, P4)
>>> C2.area
1105*pi/98
>>> C2.radius
sqrt(2210)/14
>>> C2.equation()
(x - 5/14)**2 + (y - 27/14)**2 - 1105/98
>>> C2.center
Point(5/14, 27/14)
>>> C2.circumference
sqrt(2210)*pi/7

>>> C2.intersection(C1)
[Point(55/754 + 27*sqrt(6665)/754, -5*sqrt(6665)/754 + 297/754),
 Point(-27*sqrt(6665)/754 + 55/754, 297/754 + 5*sqrt(6665)/754)]
>>> C2.intersection(S1)
[Point(3, 4)]
>>> C2.is_tangent(L2)
False
>>> C1.tangent_lines(P4)
[Line(Point(-1, 5), Point(-9/26 + 15*sqrt(17)/26, 3*sqrt(17)/26 + 45/26)),
 Line(Point(-1, 5), Point(-15*sqrt(17)/26 - 9/26, -3*sqrt(17)/26 + 45/26))]
