# lets build a set of Latin-1 chars that have the word SIGN in their Unicode
from unicodedata import name
s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)
print(name(chr(36)))
