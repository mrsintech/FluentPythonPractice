from array import array
from datetime import datetime
from random import random
import threading

# The list type is flexible and easy to use, but depending on specific requirements,
# there are better options.

# ARRAY: array saves a lot of memory when the sequence is too large.

# DEQUE: if you are constantly adding and removing items from opposite ends of a list,
# it’s good to know that a deque (double-ended queue) is a more efficient FIFO data structure.

# SET: f your code frequently checks whether an item is present in a collection,
# set is a good choice, especially if it holds a large number of items.
# sets are optimized for fast membership checking.
# NOTE: set is not a sequence.

# -=-=-=-=-=-=- ARRAYS -=-=-=-=-=-=- #
# if a list only contain numbers, an array.array is a more efficient replacement.
# array has additional methods for fast loading and saving such as .frombytes and .tofile
# a python array is as lean as c arrays.

# -=-=-=-=-=-=- List vs Array -=-=-=-=-=-=- #
# let's compair list and array speed


def arr_vs_list():
    obj_count = int(10**9)
    print("testing speed difference between list and array",
          f"obj count {obj_count}")

    print("list is building:")
    before_t = datetime.now()
    nums_l = [random() for i in range(obj_count)]
    after_t = datetime.now()
    li_time = (after_t - before_t).seconds

    print("putting list to file:")
    before_t = datetime.now()

    ar_bin_file = "nums"
# open file
# fp = open(ar_bin_file, "wb")

    after_t = datetime.now()
    li_put_time = (after_t - before_t).seconds

    print("getting list last item:")
    before_t = datetime.now()
    item = nums_l[int(obj_count-1)]
    after_t = datetime.now()
    li_get_time = ((after_t - before_t).microseconds, item)
    print("list done.", "--------------------")

    print("Building Array:")
    before_t = datetime.now()
    nums_a = array('d', (random() for i in range(obj_count)))
    after_t = datetime.now()
    ar_time = (after_t - before_t).seconds

    print("putting array to :")
    before_t = datetime.now()

# open file for writing
    fp = open(f"{ar_bin_file}_a.bin", "wb")
# now writing to the file
    nums_a.tofile(fp)
    fp.close()

# create an empty array to write in
    nums_a2 = array("d")
# open previosely close file
    fp = open(f"{ar_bin_file}_a.bin", "rb")

    nums_a2.fromfile(fp, obj_count)
    fp.close()

    after_t = datetime.now()
    li_put_time = (after_t - before_t).seconds

    print("getting array last item:")
    before_t = datetime.now()
    item = nums_a[int(obj_count-1)]
    after_t = datetime.now()
    ar_get_time = ((after_t - before_t).microseconds, item)
    print("Array Done.", "--------------------")

    print("copying list:")
    before_t = datetime.now()
    nums_l2 = []
    for i in nums_l:
        nums_l2.append(i)

    after_t = datetime.now()
    li_loop_time = (after_t - before_t).seconds

    print("copying array:")
    before_t = datetime.now()
    nums_a3 = array("d")
    for i in nums_a3:
        nums_a3.append(i)

    after_t = datetime.now()
    ar_loop_time = (after_t - before_t).microseconds

    print("Build time compair:",
          f"list took:{li_time} seconds", f"array took: {ar_time} seconds")
    print("get last item time compair:",
          f"list took:{li_get_time[0]} microseconds", f"array took: {ar_get_time[0]} microseconds")
    print("loop and copy seqs:",
          f"list took:{li_loop_time} seconds", f"array took: {ar_loop_time} microseconds")

# in tofile,from file operation processes done so fast
# read from binary files are 60 times faster than txt file
# write to binary files are 7 times faster than txt files
# size of bin file is more compact than txt file

# -=-=-=-=-=-=- End List vs Array -=-=-=-=-=-=- #

# typecode:
    tpcode = nums_a.typecode
    print(tpcode)
# type code returns one-character string identifying the C type of the item

# array does not have sort() method if sorting needed, built in sorted method
# can be used.
# a = array.array(a.typecode, sorted(a))

# creating file with 10M lines of float
    fp = open("floats-10M-lines.txt", "w+")
    ar = array("d", (random() for i in range(10**7)))
    print("array built.")
    for i in ar:
        fp.write(str(i)+"\n")
    fp.close()
