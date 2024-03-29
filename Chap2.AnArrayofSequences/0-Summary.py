"""
Core Principles in this Chapter:
    - The ABC Language
    - What is Sequence
    - Types of sequences by its way of storing data (see TypesofSequences.png)
    - Types of sequences by Mutability(see TypesofSequencesbyMutability.png)
    - list comprehensions
    - walrus operator
    - generator expressions
    - tuples
    - unpacking
    
- The ABC Language:
    the ABC in the ancestor of Python.
    Before creating Python, Guido was a contributor to the ABC language—a
    10-year research project to design a programming environment for beginners.
    ABC introduced many ideas we now consider “Pythonic”
    
    - What is Pythonic?
        generic operations on different types of sequences, built-in tuple and
        mapping types, structure by indentation, strong typing without variable
        declarations, and more. 
        It’s no accident that Python is so user-friendly.
    
- What is Sequence
    Sequences in python include types like: Strings, lists, Tuples,
    byte sequences, arrays, XML elements, and database results.
    They share a rich set of common operations, including iteration, slicing,
    sorting, and concatenation.
    
    you can create your own sequence type in python we will discuss that in
    CHAP12.

- Types of sequences by its way of storing data (see TypesofSequences.png)
    The standard library offers a rich selection of sequence types implemented
    in C:
    We have two kind of sequences:
    - Container Sequences:
        Can hold items of different types, including nested containers.
        Some examples: list, tuple, and collections.deque.
        
        - How Container Sequence Store Data?
            A container sequence holds references(pointer) to the objects it
            contains, which may be of any type

    - Flat sequences:
        Hold items of one simple type.
        Some examples: str, bytes, and array.array.
        
        - How Flat Sequence Store Data?
            flat sequence stores the value of its contents in its own memory
            space, not as distinct Python objects
            
    flat sequences are more compact, but they are limited to holding primitive
    machine values like bytes, integers, and floats. 
    Container Sequences take more space in memory but they can hold more
    types of data.
    
NOTE: arrays in python are in C
    
- Types of sequences by Mutability(see TypesofSequencesbyMutability.png):
    Another way of grouping sequence types is by mutability:
    
    - Mutable Sequences:
        are concrete classes of Immutables and their values can change.
        For example, list, bytearray, array.array, and collections.deque.
        
    - Immutable Sequences:
        For example, tuple, str, and bytes.
        
    NOTE: The built-in concrete sequence types do not actually subclass the
    Sequence and MutableSequence abstract base classes (ABCs), but they are
    virtual subclasses registered with those ABCs.


NOTE: Why flat sequences are much more compact?
    Every Python object in memory has a header with metadata
    (see TypesofSequences.png) The simplest Python object, a float, has a value
    field and two metadata fields:
    • ob_refcnt: the object’s reference count
    • ob_type: a pointer to the object’s type
    • ob_fval: a C double holding the value of the float
    On a 64-bit Python build, each of those fields takes 8 bytes. That’s why an
    array of floats is much more compact than a tuple of floats: the array is a
    single object holding the raw values of the floats, while the tuple
    consists of several objects—the tuple itself and each float object
    contained in it.

- list comprehensions:
    A quick way to build a sequence is using a list comprehension 
    (if the target is a list) or a generator expression 
    (for other kinds of sequences).
    
    the listcomps and genexp makes code more readable and faster.
    
    - Why prefer listcomps over for loop?
        because a loop can do many things, but a listcomp is more explicit.
        Its goal is always to build a new list.
    
    - Where should we not use listcomps?
        If you are not doing something with the produced list, you should not
        use that syntax. Also, try to keep it short. If the list comprehension
        spans more than two lines, it is probably best to break it apart or
        a plain old for loop.
        
    - Listcomps Scope:
        list comprehensions, generator expressions, and their siblings set and
        dict comprehensions, have a local scope to hold the variables assigned
        in the for clause.
        
        However, variables assigned with the “Walrus operator” := remain
        accessible after those comprehensions or expressions return—unlike
        local variables in a function. PEP 572—Assignment Expressions defines
        the scope of the target of := as the enclosing function, unless there
        is a global or nonlocal declaration for that target.

    - Walrus Operator :=
        The walrus operator allows you to assign a value to a variable as part
        of an expression. It helps to simplify code by allowing you to perform
        an assignment and use the assigned value in a single expression.
    
    - Map and Filter:
        Map and filter pair can use to do the listcomp job, but it adds more 
        complexity into the code and make no difference in case of performance.     
    
    PROJECT: Cartesian Product (Zarb Dekarti) with listcomps
        Listcomps can build lists from the Cartesian product of two or more
        iterables. The items that make up the Cartesian product are tuples made
        from items from every input iterable. The resulting list has a length
        equal to the lengths of the input iterables multiplied.
        [(v1, v2) for v1 in v1s for v2 in v2s]
        is equal to: 
        for v1 in v1s:
            for v2 in v2s:
                list.append((v1, v2))
    
- Generator Expressions:
    GeneratorExpressions or genexp is the equivalent of listcomp for other
    types of sequences (tuple, array , ...)
    
    Genexps use the same syntax as listcomps, but are enclosed in parentheses
    rather than brackets.

    one of the differences between genexp and listcomp is that the listcomp
    dont need to be specified to create a list e.g list[listcomp] and it just
    need to eclosed in brackets []
    but genexp need to be specified like tuple(genexp) or 
    array.array('I', (genexp))
    
NOTE: key difference between listcomp and genexp
    imagine you need a sequence to feed a for loop, the  listcomp always build
    the sequence completly if used in a for loop it first build the list and
    then feed it into for loop, but if genexp is used instead of listcomp it
    dont build sequence completey and then feed into for loop, instead it build
    the sequence one item at a time and turn loop once,hence it dont take
    resources to build a sequence just to feed a foor loop, its faster.
    
- tuples
    how tuples data store in memory? (see tupleDataStructure.png)
        the tuple contains refrences or pointers to the objects it contains
        (like lists) and if tuple contains a refrence to a list or any other 
        mutable objects, it's sub-object can change or modify but it cannot 
        delete compeletly from tuple, only item that it contains can change.
    
    tuples do double duty: 
        1- they can be used as immutable lists.
        2- as records with no field names.
    
    tuples as records with no names:
            tuples hold records, each item in tuple holds the data for one 
            field, and the position of the item gives its meaning.

        NOTE: if we have a list of tuples we can get each element of tuples
        seperatly by:
            list_of_data = [(0,1),(2,3)]
            for fn, _ in list_of_data: _ is used for unnecessary items of tuple
                print(fn)

        with tuples you can specify multiple variables at one line of code:
            city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
            this line will declare each variable with its related order in 
            tuple.
            
        NOTE: the  %s is obselete use str.format() instead.
        
        what is unpacking?
            the  for loop knows how to retirieve the items of tuple seperately,
            this is unpacking.
        
            with unpacking theres no need to go through the trouble of creating
            class just to name the fields, especially if you leverage unpacking
            and avoid using indexes to access the fields.
            the term tuple unpacking is widely used but, iterable unpacking is
            gaining traction.
        
    tuples as immutable lists:
        there's 2 key benefits in using tuples as immutable lists:
            1- calrity
                when you see a tuple you know its length is fixed.
            
            2- performance:
                a tuple uses less memory than a list of the same length.
    
    ---------------------- 15/9/23 ----------------------       
    NOTE: it's better to keep tuple mutable free. tuples with mutable items can
    be source of bugs.
    
    (N)how to determine if a tuple (or any object) has a fixed value?
        we should use hash() built-in, if an item is compeletly immutable the
        hash() will do its job flowlessly, else ((N) what type of error hash()
        will throw if object is not hashable?) it will throw TyprError
        an object is hashable if only its values cannot ever change.
    
    why tuples are widely used as immutable lists?
        (N) how a tuple generates (byte-wise) and what the difference between
        tuple and list creation?
            for tuple, python compiler generates bytecode for a tuple constant
            in !one operation! but for a list literal, the generated bytecode
            pushes each element as a seperate constant to the data stack, and
            then builds the list.   
        
        (N) how tuple() constructor behave if we feed a tuple to it? what about
        list()?
            the tuple() will make a refrence to the original tuple if we feed
            a tuple in it. it wont copy the tuple because its already immutable
            and never change.
            but the list() will copy anything feed into it.
        
        (N) why tuple is more memory efficient compared to list?
            because of its fixed length; a tuple instance is allocated the
            exact memory it needs. on the other hand list are allocated with 
            room to spare, for future appends.
            
        (N) how is tuple reference array structure (see ListStruct.png)? and
        whats its difference compared to list array reference array?
            the references to the items in tuple are stored in an array in the
            tuple struct, while a list holds !a pointer! to an array of
            references stored elsewhere.
            the extra indirection of list makes cpu caches less effective.
            
        (N) why indirection in list reference array is necessary?
            because when list grows beyond the space currently allocated,python
            needs to reallocate the array of references to make more room. 
    
    NOTE: tuples supports all list methods that do not involve adding or 
    removing items. except __reversed__ method for optimization reversed(tupel)
    still works.
    
    (N) what is list.copy()?
        it will create a shallow copy of list, which is a new list object but
        contains refrences to the same objects or elements of original list,
        any change to copied list or original list will change both  of them
        beacause they have same refrences.
        
        (N) how to copy a list to a new seperated list?
            by using new_list = list(l), l is a list
            
    (N) what is difference between list.__setitem__(p, e) and list.insert(p, e)
        they both set the item in index p to e, insert will shift items to
        right and won't delete anything, but __setitem__ will delete value of
        [p] and put e instead of it, its equal to [p] = e.
    
---- 1/10/23
- unpacking:
    unpacking is important because it avoids unnecessary and error prone use of 
    indexes to extract elements from sequences. also unpacking works with any 
    iterable object as the data source including iterators, which dont support 
    notation([]) 
    (N) why unpacking is important?
    the most visible form of unpacking is parrallel assignmant 
    e.g a, b = (12, 13) -> a=12, b=13

    an elegant application of unpacking is swapping values of variables without 
    using a temporary variable
    a, b = b, a # swapping variable
    (N) what is best way of swapping variables in python?

    with * before arguman, if arguman is a sequence the method will return multiple
    values.
    (N) what can a * do before an arguamn in function call

    ADD: os.path.split() : os.path is a module in Python's standard library that
    provides functions for working with file and directory paths in a
    platform-independent way. It allows you to manipulate file and directory paths
    regardless of whether you are running your Python code on a Windows, macOS, or
    Linux system. This module is particularly useful for writing code that needs to
    work on different operating systems without modification.
    the split() method splits a file path into two components: the directory part
    and the filename part. It returns a tuple containing these two components.

    (N) what is os.path
    (N) what is os.path.split

    Using * to grab Excess Items:
        using *args as variable will grab excess values 
        a, b, *args = range(5)
        (0, 1, [2, 3, 4])
        
        a, *body, b,c = range(5)
        (0, [1, 2], 3, 4)
        
        
        (N)whats use of *args as varables to grab excess items in parallel
        assignment and in what type of sequence it will store it?
        
        NOTE: the * can only appear onve in every parallel assignment
        (N) how mant times can we use *args in one assignment?
        
        
        

    

-=-=-=-=-=- ADDITIONALS -=-=-=-=-=-
enclosing function : 
    An "enclosing function" refers to a function that contains another
    function, often referred to as a "nested function" or "inner function."
    In Python, when a function is defined inside another function, it
    becomes a nested function, and the enclosing function is the one that
    contains the nested function.
        
lambda :
    In Python, a lambda function is a small anonymous function that can
    have any number of input parameters but can only have one
    expression. It is also known as a "lambda expression" or
    "lambda form."
    square = lambda x: x ** 2
    result = square(5)
        
map() :
    map() is a built-in function that applies a given function to all
    the items in an iterable (e.g., a list, tuple, or string) and
    returns an iterator that yields the results. It takes two or more
    arguments: the first argument is the function to apply, and the
    subsequent arguments are the iterables on which the function should
    be applied.
    
filter() : 
    In Python, filter() is another built-in function that offers a way
    to filter elements from an iterable (e.g., list, tuple, or string)
    based on a given function's conditions. It returns an iterator
    containing only the elements for which the function returns True.
    
    filter(function, iterable)
    
array.array():
    array.array is a built-in module in Python that provides an array object
    which is similar to a list, but with a more efficient memory representation
    It allows you to create arrays of a specific data type, which leads to more
    compact and faster data storage and manipulation compared to regular Python
    lists.
    the first argument in array.array defines the storage type

a little NOTE for tuple and array:
    based on my examination the tuple has less size than array if the sequence
    len is little, but it will increase more than array if items are much.
        
"""
