#!/usr/bin/python


###
#~ Creating Sets
###

x = set("A Python Tutorial")

x = set(["Perl", "Python", "Java"])

#~ no doublets are in the resulting set of cities
cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))

#~ adding member to set, sets are mutable
cities.add("Strasbourg")

#~ Frozensets are like sets except that they cannot be changed,  they are immutable
	#~ 'frozenset' object has no attribute 'add'
cities = frozenset(["Frankfurt", "Basel","Freiburg"])

#~ We can define sets using curly braces
adjectives = {"cheap","expensive","inexpensive","economical"}


###
#~ Set Operations
###

#~ add(element)

>>> colours = {"red","green"}
>>> colours.add("yellow")
>>> colours
set(['green', 'yellow', 'red'])

#~ remove all elements from a set

>>> cities = {"Stuttgart", "Konstanz", "Freiburg"}
>>> cities.clear()
>>> cities
set([])

#~ copy

>>> more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
>>> cities_backup = more_cities.copy()
>>> more_cities.clear()
>>> cities_backup
set(['St. Gallen', 'Winterthur', 'Schaffhausen'])

#~ difference()

	#way 1
>>> x = {"a","b","c","d","e"}
>>> y = {"b","c"}
>>> z = {"c","d"}
>>> x.difference(y)
set(['a', 'e', 'd'])
>>> x.difference(y).difference(z)
set(['a', 'e'])

	#way 2
>>> x - y
set(['a', 'e', 'd'])
>>> x - y - z
set(['a', 'e'])

#~ difference_update()

	#way 1
>>> x = {"a","b","c","d","e"}
>>> y = {"b","c"}
>>> x.difference_update(y)

	#way 2
>>> x = {"a","b","c","d","e"}
>>> y = {"b","c"}
>>> x = x - y
>>> x
set(['a', 'e', 'd'])

#~ discard() # no error

>>> x = {"a","b","c","d","e"}
>>> x.discard("a")
>>> x
set(['c', 'b', 'e', 'd'])
>>> x.discard("z")
>>> x
set(['c', 'b', 'e', 'd'])

#~ remove() # will give error if element not exists

>>> x = {"a","b","c","d","e"}
>>> x.remove("a")
>>> x
set(['c', 'b', 'e', 'd'])
>>> x.remove("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'

#~ intersection()

	#way 1
>>> x = {"a","b","c","d","e"}
>>> y = {"c","d","e","f","g"}
>>> x.intersection(y)
set(['c', 'e', 'd'])

	#way 2
>>> x = {"a","b","c","d","e"}
>>> y = {"c","d","e","f","g"}
>>> x  & y
set(['c', 'e', 'd'])

#~ isdisjoint()
	#~ This method returns True if two sets have a null intersection.


