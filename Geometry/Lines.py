>>> L1 = Line(P1, P2)
>>> L2 = L1.perpendicular_line(P3)  # perpendicular line to L1
>>> L2.arbitrary_point()            # parametric equation of L2
Point(4*t + 2, -3*t - 1)
>>> L2.equation()                   # algebraic equation of L2
3*x + 4*y - 2
>>> L2.contains(P4)                 # is P4 in L2?
False
>>> L2.distance(P4)                 # distance from P4 to L2
3
>>> L1.is_parallel(S2)              # is S2 parallel to L1?
False
