"""
Python – Value length dictionary
"""

"""
Method #1: Using loop + len()
"""

# Vale length dictionary
# Using loop + len()

# Initializing dictionary
test_dict = {1:'VJH', 2:'IS', 3:'Best'}

# printing original dictionary
print(" The original dictionary is:" + str(test_dict))
# ->  The original dictionary is:{1: 'VJH', 2: 'IS', 3: 'Best'}

# value length dictionary
# Using loop + len()

res = {}
for val in test_dict.values():
    res[val] = len(val)
# Printing result
print("The value-size mapped dictionary is:" + str(res))
# -> The value-size mapped dictionary is:{'VJH': 3, 'IS': 2, 'Best': 4}

"""
Method #2: Using dictionary comprehension
"""

# Initializing dictionary
test_dict = {1:'a', 2:'b', 3:'c'}

# Printing original dictionary
print("The original dictionary is:"+ str(test_dict))
# -> The original dictionary is:{1: 'a', 2: 'b', 3: 'c'}

# Value length dictionary
# Using dictionary comprehension
res = {val: len(val) for val in test_dict.values()}

#printing result
print("The value-size mapped dictionary is:" +str(res))
# -> The value-size mapped dictionary is:{'a': 1, 'b': 1, 'c': 1}


"""
Method #3: Here is another approach using map and len functions:
"""

# Initializing dictionary
test_dict = {1:'a', 2:'b', 3:'c'}
print("this is the first dictionary:" + str(test_dict))
# -> this is the first dictionary:{1: 'a', 2: 'b', 3: 'c'}

# Value length dictionary
# Using map() and len()
res =  dict(map(lambda x: (x[1], len(x[1])), test_dict.items()))
print("The value-size mapped dictionary is:" + str(res))
# -> The value-size mapped dictionary is:{'a': 1, 'b': 1, 'c': 1}

"""
Method #4: Using collections.defaultdict() and loop
"""

from collections import defaultdict

# initializing dictionary
test_dict = {1:'a', 2:'b', 3:'c'}
print("the original dictionary is:" + str(test_dict))
# -> the original dictionary is:{1: 'a', 2: 'b', 3: 'c'}

#value length dictionary using defaultdict and loop
res = defaultdict(int)
for val in test_dict.values():
    res[val] = len(val)
print("The value-size mapped dictionary is:" + str(dict(res)))
# ->The value-size mapped dictionary is:{'a': 1, 'b': 1, 'c': 1}



