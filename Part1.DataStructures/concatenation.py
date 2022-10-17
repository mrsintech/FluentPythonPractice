
# -=-=-=-=-=-=-=-=- concatenation -=-=-=-=-=-=-=-=- #
# in python we expect that sequences support + and *
# usually both operands of + must be the same sequence type,
# and neither of them modified, but a new squence of the same type
# is created as result of the concatenation.

a = [1, 2, 3]
b = [4, 5, 6]
res = a + b


# to concatenate multiple copies of the same sequence, multiply it by an integer.
res = a * 4

res = ("abc-" * 5).rstrip("-")
print(res)
# so, if multiply a sequence in an integer the result is multiple copies of that seq.
# PRO TIP: both + and * always create a new object, and never change their operands.

# what about nested sequences?
a = [[1, 2, 3], (4, 5), 6]
res = a * 3
res[0][0] = 22
# as you can see the inner lists are refrences to the original list, now if you
# perform print(a) the first item of first inner list will be 22, but we changed
# the first list in res var!

# ========= tic-tac-toe board ========= #
# for practice lists in lists
board = [['_'] * 3 for i in range(3)]
# if use board = [['_'] * 3] * 3 instead of listcomp by changing 1 item of list all will change
board[1][2] = 'X'

# ========= Augmented assignment with sequences ========= #
# now we discuss += and *= operators, because they produce different very
# different results, depending on mutability of the target sequence.

# not related tip: if __iadd__ not implemented, python falls back to calling
# __add__
a = [1, 2, 3]
b = [4, 5, 6]
a += b  # a is changed in place (the effect will be similar to a.extend(b))

a = (1, 2, 3)
b = (4, 5, 6)
a += b
# for immutable squences the original seq will remove and a new sequence will replace.

# the *= operator behave similar to += for mutable and immutable sequences

# repeated concatenation of immutable sequences is inefficient, cuz instead of
# just appending new items, the interpreter has to copy the hole target sequence
# to create new one with the new items concatenated.

# i just found dis.dis :))
# dis.dis('a = [i for i in range(99999999999999999999999999)]')

# ProTip: Avoid using mutable items in tuple

print(res)
