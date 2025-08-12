"""
Python Program for Array Rotation Example
"""

# Python program to left-rotate the given array

# Function reverse the given array
# by swapping first and last numbers.

def reverse (start, end, arr):
    #No of iteractions needed for reversing the list
    no_of_reverse = end - start + 1

    #by incrementing count value swapping
    # of first and last elements is done.
    count = 0
    while((no_of_reverse)//2 != count):
        arr[start + count], arr[end - count] =  arr[end-count], arr[start+count]
        count += 1
    return arr

# Funtion takes array, length of
#array ad no rotations as input

def left_rotate_array(arr, size, d):
    # Reverse the Entire List
    start = 0
    end = size - 1
    arr = reverse(start, end, arr)

    # Divide array into twosub-array.
    # based on no of rotations.
    # divide first sub-array.
    # reverse the first sub-array.
    start = 0
    end = size-d-1
    arr = reverse(start, end, arr)

    # Divide Second sub-array
    # Reverse the second sub-array
    start = size-d
    end = size - 1
    arr = reverse(start, end, arr)
    return arr

arr = [1,2,3,4,5,6,7,8]
size = 8
d = 1
print("Original Array:", arr)

#finding all the sysmmetric rotation number
if (d <= size):
    print("rotate array: ", left_rotate_array(arr, size, d),'\n---')
else:
    d = d % size
    print('Rotate array: ', left_rotate_array(arr, size, d),'\n---')

"""
Python Program for Array Rotation Using temp array

Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n = 7 
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
"""

def rotateArray (arr, n, d):
    temp = []
    i=0
    while(i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while(d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[:] + temp
    return arr

#driver function to test above function
arr = [1,2,3,4,5,6,7]
print("Array after left rotation is:", end=' ')
print(rotateArray(arr, len(arr),2))


"""
Python Program for Array Rotation Using Rotate one by one

leftRotate(arr[], d, n)
start
  For i = 0 to i < d
    Left rotate all elements of arr[] by one
end
"""

#Function to left rotate arr[] of size n by d*/
def leftRotate (arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

#Function to left rotate aar[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp =  arr[0]
    for i in range (n-1):
        arr[i] = arr[i+1]
        arr[n-1] = temp

#utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print ("%d"% arr[i],end=" ")

#driver  program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7, 8]
leftRotate(arr, 2, 7)
print(arr, 7)


"""
Python Program for Array Rotation Using 4 Juggling Algorithm

a)    Elements are first moved in first set – (See below diagram for this movement
ArrayRotation
          arr[] after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}

b)    Then in second set.
          arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}

c)    Finally in third set.
          arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}
"""

def leftRotate(arr, d, n):
    for i in range (gcd(d, n)):
        #move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k =j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] =  temp
#UTILITY FUNCTIONS
#Functions to print an array

def printArray (arr, size):
    for i in range (size):
        print("%d" % arr[i], end=" ")

#Function to get gcd of a and b
def gcd (a, b):
    if  b == 0:
        return a
    else:
        return gcd(b, a % b)

# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

"""
python program using the list
slicing approach to rotate the array

Programa de python que usa la lista
enfoque de segmentacion de la matriz
"""
def rotateList(arr, d, n):
    arr[:]= arr [d : n] + arr [0:d]
    return arr

# Driver fucntion to test above the function
# funcion del controlador para probar la funcion anterior.
arr = [1, 2, 3, 4, 5, 6]
print (arr)
print("Rotated list is")
print(rotateList(arr, 2, len(arr)))

