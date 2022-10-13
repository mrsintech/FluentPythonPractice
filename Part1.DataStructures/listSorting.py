
# -=-=-=-=-=-=- list.sort vs built-in sorted -=-=-=-=-=-=- #
# the list.sort method sorts a list in place, without making a copy
# NOTE: important Python API convention: functions or methods that return None,
    # that means they changed the object in place and no new object is created.

li = ["tywin", "daenerys", "Tyrion", "johnsnow"]
li.sort()
res = li

# but, the built-in sorted method, creates a new object (list) and returns it.
    # therefor it can accept any object including immutable sequences and generatos.
li = ["tywin", "daenerys", "Tyrion", "johnsnow"]
res = sorted(li)

# both reversed and list.sort() take two optional keyword-only args:
li = ["tywin", "daenerys", "Tyrion", "johnsnow"]
# reverse:
li.sort(reverse=True)

res = sorted(li, reverse=True)

# key:
# key is a 1 arg function that will applied to each item to produce its sorting key.
# default of key is the identity function
res = sorted(li, key=str.lower) # compare case-insensitive
res = sorted(li, key=len) # compare by length of item
res = sorted(li, key=max)

# that can be very useful, NICE!



print(res)
print(max("johnsnow"))



















