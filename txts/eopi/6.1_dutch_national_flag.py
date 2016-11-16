import random
import time
import sys

# Credits:
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/DutchNationalFlagSlowInplace.java
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/DutchNationalFlagTwoPasses.java
# https://github.com/adnanaziz/epicode/blob/master/java/src/main/java/com/epi/DutchNationalFlag.java

def dutch_flag_partition_slow(pivot_index, a):
	""" O(n^2) Time & O(1) Space """
	pivot = a[pivot_index]
	
	# First pass: group elements smaller than pivot.
	i = 0
	while i < len(a):
		j = i + 1
		# Look for a smaller element.
		while j < len(a):
			if a[j] < pivot:
				a[i], a[j] = a[j], a[i]
				break
			j += 1
		i += 1
	
	# Second pass: group elements larger than pivot.
	i = len(a) - 1
	while i >= 0 and a[i] >= pivot:
		j = i - 1
		# Look for a larger element. Stop when we reach an element less
		# than pivot, since first pass has moved them to the start of a.
		while j >= 0 and a[j] >= pivot:
			if a[j] > pivot:
				a[i], a[j] = a[j], a[i]
				break
			j -= 1
		i -= 1
	
	
def dutch_flag_partition_two_pass(pivot_index, a):
	""" O(n) Time & O(1) Space """
	pivot = a[pivot_index]
	
	# First pass: group elements smaller than pivot
	i = 0
	smaller = 0
	while i < len(a):
		if a[i] < pivot:
			a[i], a[smaller] = a[smaller], a[i]
			smaller += 1
		i += 1
	
	# Second pass: group elements larger than pivot
	i = len(a) - 1
	larger =  len(a) - 1
	while i >= 0 and a[i] >= pivot:
		if a[i] > pivot:
			a[i], a[larger] = a[larger], a[i] 
			larger -= 1
		i -= 1
	
	
def dutch_flag_partition_one_pass(pivot_index, a):
	""" O(n) Time & O(1) Space """
	pivot = a[pivot_index]
	
	# Keep the following invariants during partitioning:
	# bottom group: a[0:smaller]
	# middle group: a[smaller:equal]
	# unclassified group: a[equal:larger]
	# top group: a[larger:len(a)]
	smaller = 0
	equal = 0
	larger = len(a)
	
	# Keep iterating as long as there is an unclassified element.
	while equal < larger:
		# a[equal] is the incoming unclassified element.
		if a[equal] < pivot:
			a[smaller], a[equal] = a[equal], a[smaller]
			smaller += 1
			equal += 1
		elif a[equal] == pivot:
			equal += 1
		else:  # a[equal] > pivot
			larger -= 1
			a[equal], a[larger] = a[larger], a[equal]
	
	
def dutch_flag_partition_unit_test(dutch_flag_partition):
	"""Test a random list and pivot, 1000 times."""
	for i in range(1000):
		n = random.randrange(1, 100)
		a = rand_list(n)
		a_dup = list(a)
		
		pivot_index = random.randrange(0, n)
		pivot = a[pivot_index]

		dutch_flag_partition(pivot_index, a)
		
		if not check(pivot, a, a_dup):
			sys.exit(0)
			
	print "All tests passed for " + dutch_flag_partition.__name__
	
	
def rand_list(size):
	l = []
	for i in range(size):
		l.append(random.randrange(0, 10))
	return l
	
	
def check(pivot, a, a_dup):
	n = len(a)
	i = 0
	while i < n and a[i] < pivot:
		i += 1
	while i < n and a[i] == pivot:
		i += 1
	while i < n and a[i] > pivot:
		i += 1
		
	if not i == n:
		print "\nError with function: " + dutch_flag_partition.__name__
		print "Before: [" + ",".join([str(x) for x in a_dup]) + "]"
		print "\t After: [" + ",".join([str(x) for x in a]) + "]"
		sys.exit(0)
			
	return True
	
	
if __name__ == "__main__":
	dutch_flag_partition_unit_test(dutch_flag_partition_slow)
	dutch_flag_partition_unit_test(dutch_flag_partition_two_pass)
	dutch_flag_partition_unit_test(dutch_flag_partition_one_pass)

	

	
	
	
	

	
	
	
	
