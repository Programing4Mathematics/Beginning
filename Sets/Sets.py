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

