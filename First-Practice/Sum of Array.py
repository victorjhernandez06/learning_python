"""
Program to find sum of Array
input : arr[]  = {1, 2, 3}
Output: 6
Explanation: 1 + 2 + 3 = 6
"""

def _sumar(arr):
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0

    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum  = sum + i
    return(sum)

# main function
if __name__ == "__main__":
    #input values to list
    arr = [12, 3, 4, 15]

    #calculating length of array
    n = len (arr)
    # calling function ans store the sum in ans
    ans = _sumar(arr)
    # display sum
    print('Sum of the array is: ', ans,'\n---')


# Python Program to Find Sum of Array Using sum()
    #input values to list
    arr = [22, 3, 4, 15]

    #sum() is an inbuilt function in python that adds
    #all the elements in list, set and tuples and returns
    #the value
    ans = sum(arr)

    #display sum
    print('Sum of the array is:', ans,'\n---')

"""
Program to find SUM of Array using reduce method
"""
from functools import reduce

def _sum(arr):
    # iterate over array
    #using reduce and get
    #sum on acummulator
    sum =  reduce(lambda a, b: a+b, arr)
    return (sum)

#driver function
arr = []
#input values to list
arr = [12, 3, 4, 15]

#calculating lentgh of array
n = len (arr)

ans =  _sum(arr)

#display sum
print('sum of the array is:', ans,'\n---')

"""
Python Program to Find Sum of Array Using enumerate function 
"""

list1 = [12, 3, 4, 15]; s=0
for i, a in enumerate(list1):
    s+=a
print('sum of de array is:',s,'\n---')


"""
Python Program to Find Sum of Array Using Divide and conquer
"""
def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high)//2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum
#examples
arr = [1, 2, 3]
print(sum_of_array(arr,0 , len(arr)-1))

arr=[15,12,13,10]
print(sum_of_array(arr, 0, len(arr)-1),'\n---')

"""
Python Program to Find Sum of Array Using counter method.
"""
from collections import Counter

arr =  [12, 3, 4, 15]
c = Counter(arr)
sum = 0

for key, value in c.items():
    sum += key * value

print('Sum of the array is:', sum,'\n---')
