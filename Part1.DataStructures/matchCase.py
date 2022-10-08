# Match Case Basic 
"""
Match/case is like switch/case in C lang but one improvment of match over 
switch is destructurin. a more advanced form of unpacking 
"""
status = (1, "foo")
status = (1, "foo", "bar")
status = (2, "foo", "bar", "baz")
match status:
    case [1, anything]: # sequences type in subject and case can differ and the result dont change
        print(anything)
        
    case [1, i, a]: # the 1 in the beginning of sequence isn't effective if len of status doesn't match
        print(a)
        
    case _: # Default case if nothing match above cases this case will execute
        raise Exception("What are you doing?")