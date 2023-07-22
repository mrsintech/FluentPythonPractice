from array import array
from locale import MON_1

# -=-=-=-=-=-=- MEMORY VIEW -=-=-=-=-=-=- #
# the built-in memoryview class is a shared-memory sequence type that lets you
# handle slices of arrays without copying bytes.

# the memoryview.cast method lets you change the way multiple bytes are read or
# written as units without moving bits around.


octest = array('B', range(6))

# building memoryview from array
m1 = memoryview(octest)
m1_l = m1.tolist()
print(m1_l)

m2 = m1.cast("B", [2, 3])
m2_l = m2.tolist()
print(m2_l)

m3 = m1.cast("B", [3, 2])
m3_l = m3.tolist()
print(m3_l)

m2[1, 1] = 44  # type: ignore
m3[1, 1] = 33  # type: ignore

print(octest)
# so, every change i make to octest, m1, m2, m3 every one of then will change,
# because they share same memory.

# if the array is not in bytes, the memory view can be a bad choice!
nums = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(nums)
print(memv[0])

memv_oct = memv.cast("B")
print(memv_oct.tolist())
memv_oct[5] = 4
print(nums)
