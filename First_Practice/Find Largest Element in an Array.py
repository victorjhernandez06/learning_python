"""
Find Largest Element in an Array

Input : arr[] = {10, 20, 4}
Output : 20
Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
"""

# Find largest element in an array Using Native Approach

def largest(arr,n):
    #initialize maximun element
    max = arr[0]

    #traverse array elements from second
    # and compare every element with
    # current Max

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

#driver code
arr = [10, 324, 45, 90, 9080]
n = len (arr)
Ans = largest(arr, n)
print("Largest in given  array is:", Ans)

"""
Find largest element in an array Using built-in function max()
"""
def largest(arr, n):
    ans = max(arr)
    return ans;

#driver code
if __name__ == '__main__':
    arr = [10, 324, 90, 45, 9080]
    n =  len(arr)
    print ("largest in given array is:", largest(arr, n))


"""
Find largest element in an array Using sort() function
"""
# program python to find maximum
# in arr[] of size n

def largest(arr, n):
    # sort the array
    arr.sort()

    # the last element of the
    # array is the largest element
    return arr[n-1]
    # or return arr[-1]

# Driver Code
arr = [10, 324, 45, 90, 9080]
n = len (arr)
Ans = largest(arr, n)
print("Largest in given array", Ans)


"""
Find largest element in an array Using reduce() function
"""

from functools import reduce

def largest (arr):
    #sort the array
    ans = reduce(max, arr)

    return ans
    # or returning largest value

# Driver Code
arr = [10, 324, 45, 90, 9080]
n = len(arr)
Ans = largest(arr)
print("largest in given array", Ans,'\n---')

"""
Find largest element in an array Using operator.gt()
"""

import operator
#initializing the list
arr = [2, 1, 7, 3, 0]
max = 0

#printing the original list
print('the given array is:', arr)
# checking for large element
for i in arr:
    if operator.gt(i,max):
        max = i
#printing the large number in the array
print("The biggest number in the given array is:", max);

"""
Find Largest Element with Python Lambda
"""

array = [10, 5, 20, 8, 15]

largest_element = max(array, key=lambda x: x)
print("Largest element in the array:", largest_element)
