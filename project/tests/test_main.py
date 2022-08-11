import sys
sys.path.insert(0, "/home/noise/Documents/pytests/project")
from my_sum import sum

def test_sum():
	assert sum([1, 2, 3]) == 6, "Should be 6"

def test_tuple():
	assert sum((1, 2, 3)) == 6, "should be 6"

def test_string():
	assert sum("lol") == 6, "should be 6"

def test_floats():
	assert sum([1.0, 2.0, 3.0]) == 6.0, "should be 6"

def test_negative():
	assert sum([-1, -2, -3]) == -6, "should be -6"

def test_single():
	assert sum(1) == 6, "should be 6"

