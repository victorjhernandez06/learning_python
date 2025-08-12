"""Python Iterators"""
# an iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

"""Iterator vs Iterable"""
# List, tuples, dicctionaries, and sets are iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# Example: Return an iterator from a tuple, and print each value:
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit)) #--> apple
print(next(myit)) #--> banana
print(next(myit)) #--> cherry

# Even strings are iterable objects, and can return an iterator
# Example: Strings are also iterable objects, containing a sequence of characters:
mystr = 'banana'
myit = iter(mystr)

print(next(myit)) #--> b
print(next(myit)) #--> a
print(next(myit)) #--> n
print(next(myit)) #--> a
print(next(myit)) #--> n
print(next(myit)) #--> a

"""Looping Through an iterator """
# We can also use a for loop to iterate through an iterable object/
# Example: iterate the values of a tuple:
mystr1 = ('Apple')
for x in mystr1:
    print(x)

# the for loop actually creates an iterator object and executes the next() method each loop.

"""Create an Iterator"""
# To create an object/class as an iterator you have to implement the methods __iter__() an __next__() to your Object.
# As you have learned in the python classes/objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similiar, you can do operations (initializing etc.) but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# Example: Create an iterator that returns numbers, starting with 1, and each sequence will increase by one( returning 1,2,3,4,5 etc.)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter (myclass)

print(next(myiter)) # --> 1
print(next(myiter)) # --> 2
print(next(myiter)) # --> 3
print(next(myiter)) # --> 4
print(next(myiter)) # --> 5

"""StopIteration"""

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration form going on forever, we can use the stopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times.

# Example: Stop after 20 iterations.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

