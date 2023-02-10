"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

#def simple_work_calc(n, a, b):
#	if n <= 1:
#		return n
#	else:
#		return a * simple_work_calc(n//b, a, b) + n

#
#def test_simple_work():
	#	assert simple_work_calc(10, 2, 2) == 36
	# assert simple_work_calc(20, 3, 2) == 230
	# assert simple_work_calc(30, 4, 2) == 650
	# assert simple_work_calc(40,5,2) == 5390
  # assert simple_work_calc(50,10,2) == 137500
  # assert simple_work_calc(60,3,2) == 960

 # pass

def work_calc(n, a, b, f):
#	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

#	Params:
#	n......input integer
#a......branching factor of recursion tree
#b......input split factor
#f......a function that takes an integer and returns 
#the work done at each node 

#Returns: the value of W(n).

	if n == 0:
		return 0
	elif n == 1:
		return f(1)
	else:
		return a * work_calc(n//b, a, b, f) + f(n)


def span_calc(n, a, b, f):
#	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

#	Params:
#	n......input integer
#	a......branching factor of recursion tree
#	b......input split factor
#	f......a function that takes an integer and returns 
#           the work done at each node 

#	Returns: the value of W(n).
#	"""
	if n <= 0:
		return n
	else:
		return span_calc(n//b, a, b, f) + f(n)

#def test_work():
#	""" done. """
#	assert work_calc(10, 2, 2,lambda n: 1) == 15
#	assert work_calc(20, 1, 2, lambda n: n*n) == 530
#	assert work_calc(30, 3, 2, lambda n: n) == 300
# assert work_calc(50, 4, 2, lambda n: n*3) == 7554
# assert work_calc(100, 2, 2, lambda n: 25) == 3175
# assert work_calc(10, 5, 2, lambda n: n^3) == 314

def compare_work(sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
#	"""
#	Compare the values of different recurrences for 
#	given input sizes.

#	Returns:
#	A list of tuples of the form
#	(n, work_fn1(n), work_fn2(n), ...)
	
	#"""
	result = []
	for n in sizes:
		#compute W(n) using current a, b, f
		result.append((n, work_calc(n, 4, 2, lambda n: n), work_calc(n, 4, 2, lambda n: n^3), work_calc(n, 4, 2, lambda n: n^2)))
	return result

#def print_results(results):
	#""" done """
	#print(tabulate.tabulate(results,
	#						headers=['n', 'W_1', 'W_2'],
	#						floatfmt=".3f",
#							tablefmt="github"))


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	def work_fn1(n):
		work_calc(n, 4, 2, lambda n: n)
	def work_fn2(n):
		work_calc(n, 4, 2, lambda n: n^3)

	res = compare_work(work_fn1, work_fn2)
	print(res)

#def test_compare_span():
	# TODO
#"""