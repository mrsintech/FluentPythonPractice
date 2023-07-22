import sys

l1 = [0, 1, 2, 3]
l2 = l1
print(sys.getsizeof(l1))
l1.append(4)
print(sys.getsizeof(l1))
val = l1.pop()

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
di = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10
}

print(sys.getsizeof(li))
print(sys.getsizeof(di))


# How to copy list
a = [1, 2, 3]
b = list(a)
b[1] = 32
print(a)  

