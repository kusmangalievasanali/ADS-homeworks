#Task1
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n, end=" ")
n = int(input("Enter a number: "))
print_numbers(n)

#Task2
def print_numbers(n):
    print(n, end=" ")
    if n == 0 or n == 1:
        return
    print_numbers(n-1)
n = int(input("Enter a number: "))
print_numbers(n)

#Task3
def numbers(n):
    if n == 0:
        return 0
    return numbers(n-1)+n
n = int(input("Enter a number: "))
print(numbers(n))

#Task4
def numbers(n):
    if n<=1:
        return 1
    return numbers(n-1)*n
n = int(input("Enter a number: "))
print(numbers(n))

#Task5
def numbers(a,b):
    if b==1:
      return a
    return numbers(a,b-1)*a
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(numbers(a,b))

#Task6
def numbers(a):
    if a==0:
        return 0
    return a%10+numbers(a//10)
a = int(input("Enter a number: "))
print(numbers(a))

#Task7
def numbers(a):
    if a==0:
        return
    numbers(a // 10)
    cnt.append(a%10)
a = int(input("Enter a number: "))
cnt = []
numbers(a)
print(len(cnt))

#Task8
def print_numbers(n):
    if n == 0:
        return
    print(n%10,end="")
    print_numbers(n//10)
n = int(input("Enter a number: "))
print_numbers(n)

#Task9
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
n = int(input("Enter a number: "))
print(fib(n))

#Task10
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

s = input("Enter a word: ")
if palindrome(s):
    print("Palindrome")
else:
    print("Not palindrome")

#Task11
def summa(n):
    if n == 0:
        return 0
    return arr[n-1] + summa(n-1)
arr = [int(input()) for i in range(int(input("count of element: ")))]
print(summa(len(arr)))

#Task12
def maximumum(n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], maximumum(n - 1))
arr = [int(input()) for i in range(int(input("count of element: ")))]
print(maximumum(len(arr)))

#Task13
def count(arr, n):
    if n == 0:
        return 0
    if arr[n-1] == target:
        return 1 + count(arr, n-1)
    else:
        return count(arr, n-1)
arr = [int(input()) for i in range(int(input("count of element: ")))]
target = int(input("target number: "))
print(count(arr, len(arr)))

#Task14
def find(arr, n):
    if n == 0:
        return False
    if arr[n-1] == target:
        return True
    else:
        return find(arr, n-1)
arr = [int(input()) for i in range(int(input("count of element: ")))]
target = int(input("target number: "))
if find(arr, len(arr)):
    print("Found")
else:
    print("Not found")

#Task15
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr[1:])
arr = [int(input()) for i in range(int(input("count of element: ")))]
if is_sorted(arr):
    print("Sorted")
else:
    print("Not sorted")

#Task16
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target, mid+1, right)
arr = [int(input()) for i in range(int(input("count of element: ")))]
target = int(input("target number: "))
index = binary_search(arr, target, 0, len(arr)-1)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
