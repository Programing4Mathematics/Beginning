>>> T.reflect(L1)
Triangle(Point(0, 0), Point(3, 4), Point(-38/25, 41/25))
>>> T.rotate(pi/2, P2)
Triangle(Point(7, 1), Point(3, 4), Point(8, 3))
>>> T.translate(5,4)
Triangle(Point(5, 4), Point(8, 8), Point(7, 3))
>>> T.scale(9)
Triangle(Point(0, 0), Point(27, 4), Point(18, -1))
>>> Arc.rotate(pi/2, P3).translate(pi,pi).scale(0.5)
Curve((-2.0*sin(t) + 0.5 + 0.5*pi, 3*cos(t) - 3 + pi), (t, 0, 3*pi/4))