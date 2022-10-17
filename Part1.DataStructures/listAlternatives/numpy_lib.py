from time import perf_counter as pc
from time import sleep

import numpy as np

# -=-=-=-=-=-=- NUMPY -=-=-=-=-=-=- #
# for advanced array and matrix  operations, numpy is the reason why python
# became mainstream in scientific computing applications. NumPy implements
# multi- dimensional, homogeneous arrays and matrix types that hold
# not only numbers but also user-defined records, and provides efficient
# element-wise operations.

# SciPy is a library, written on top of NumPy, offering many scientific
# computing algo‐ rithms from linear algebra, numerical calculus, and
# statistics. SciPy is fast and reliable because it leverages the widely
# used C and Fortran codebase from the Netlib Reposi‐ tory.

a = np.arange(12)
print(a)
print(type(a))
# ndarray means N-dimentional array
print(a.shape)

# lets add one dimention
a.shape = 3, 4
print(a.shape)
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 1])
a.transpose()  # means swap columns with rows

# load data from file
floats = np.loadtxt("floats-10M-lines.txt")
print(floats[-3:])
floats *= 2
print(floats[-3:])

# perf_counter the high-resolution performance measurement timer
t0 = pc()
floats /= 3
t0 = pc() - t0
print(t0)
# save array in .npy binary file
np.save('floats-10M', floats)
# load array from file
# load data as a memory-mapped file into another array.
floats2 = np.load('floats-10M.npy', "r+")
floats2 *= 6
print(floats2[-3:])
print(type(floats2))


# perf_counter is a high-resolution (high precision) timer.
# perf_counter_ns return value as nanoseconds

# ways to save array to file:
# file open().write
# array.tofile()
# numpy.save(file, array)
