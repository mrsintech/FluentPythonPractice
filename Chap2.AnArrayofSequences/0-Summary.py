"""
Core Principles in this Chapter:
    - The ABC Language
    - What is Sequence
    - Types of sequences by its way of storing data (see TypesofSequences.png)
    - Types of sequences by Mutability(see TypesofSequencesbyMutability.png)
    - list comprehensions
    
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
            A container sequence holds references to the objects it contains,
            which may be of any type

    - Flat sequences:
        Hold items of one simple type.
        Some examples: str, bytes, and array.array.
        
        - How Flat Sequence Store Data?
            flat sequence stores the value of its contents in its own memory
            space, not as distinct Python objects
            
    flat sequences are more compact, but they are limited to holding primitive
    machine values like bytes, integers, and floats. 
    But Container Sequences take more space in memory but they can hold more
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
    


"""
