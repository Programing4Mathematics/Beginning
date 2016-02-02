>>> from sympy import var, pi, sin, cos
>>> var('t', real=True)		# "t" - the parameter
>>> Arc = Curve((3*cos(t), 4*sin(t)), (t, 0, 3*pi/4))		#  parametric equations, the interval of the parameter.
