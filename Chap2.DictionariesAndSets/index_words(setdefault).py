from collections import defaultdict
import re
import sys

WORD_RE = re.compile(r'\w+')

try:
    file = sys.argv[1]

except IndexError:
    file = 'Chap2.DictionariesAndSets/zen.txt'

index = {}
with open(file, encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):  # enumerate(iterable, start_from)
        # finditer search for matches with WORD_RE and yields them one by one
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            loc = (line_no, column_no)
            occu = index.get(word, [])
            occu.append(loc)
            index[word] = occu  # Put changed occurrences into index dict;
            # this entails a second search through the index.

# A better way to doing this precedure. The three lines dealing with
# occurrences can be replaced by a single line using dict.setdefault.
index = {}
with open(file, encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):  # enumerate(iterable, start_from)
        # finditer search for matches with WORD_RE and yields them one by one
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            loc = (line_no, column_no)
            index.setdefault(word, []).append(loc)  # Get the list of
            # occurrences for word, or set it to [] if not found; setdefault
            # returns the value, so it can be updated
            # without requiring a second search. <-----------------------------

# even better?
# we can use defaultdict
index = defaultdict(list)
with open(file, encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):  # enumerate(iterable, start_from)
        # finditer search for matches with WORD_RE and yields them one by one
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            loc = (line_no, column_no)
            index[word].append(loc)

# display words in sorted
for word in sorted(index.keys(), key=str.upper):
    print(word, index[word])

# the first code performs at least two searches for key while setdefault does
# it all with a single lookup.

# testing for myself
di = dict(a=[1], b=[2], c=[3])
print(di)
di.setdefault('a', []).append(10)
print(di)
# i conclude that .setdefault can change sequences in place not completely
# change the value ofspecific key.
