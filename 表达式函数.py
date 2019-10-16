import numpy as np
import os,sys

dt = np.dtype([('age',np.int64)])

num = 0
def quicksort(arr):
    global num
    num += 1
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)




# Prints "[1, 1, 2, 3, 6, 8, 10]"

nlist = [3,6,8,4,10,1,2,1,7,5,11,83,75,84,36,72,25,18,91,67,53]

# nlist.sort()
# nlist.reverse()
# print(nlist)
numlist = []

def sortquick(arr):
    if len(arr) == 0:
        return
    mnum = (max(arr))
    arr.pop(arr.index(mnum))
    numlist.append(mnum)
    return sortquick(arr)

def square(num):
    return num*2

f = lambda num:num+num


def test(x):
    return x*x


nlist.append(f(10))


#lambda 表达式
s = lambda x,y:x**y

l2=map(s,range(1,100,10),range(1,100,10))

def sums(x,y):
    print("{}*{}={}".format(x,y,x*y))
    return x*y
import functools
from functools import reduce


hh = list(range(1,10))
hh.reverse()

# map 循环执行，返回list
print(list(map(sums,range(1,10),range(1,10))))


# reduce 相邻两个数操作
print(reduce(sums,range(1,10)))

