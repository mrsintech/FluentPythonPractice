"""
Bold subjects in this chapter:
    - Magic Methods
    - How to use Special methods
    - Collection API
    - Why len() is not a method
    - What is python coding style?

    

Magic Method:
    when we leverage the Python Data Model to build new classes. The Python
    interpreter invokes special methods to perform basic object operations,
    often triggered by special syntax. The special method names are always
    written with leading and trailing double underscores. For example, the
    syntax obj[key] is supported by the __getitem__ special method. In order to
    evaluate my_collection[key], the interpreter calls
    my_collection.__getitem__(key).
    
    The first thing to know about special methods is that they are meant to be
    called by the Python interpreter, and not by you. You don’t write
    my_object.__len__(). You write len(my_object) and, if my_object is an
    instance of a user-defined class, then Python calls the __len__ method you
    implemented.
    
    NOTE: the interpreter takes a shortcut when dealing for built-in types like
    list, str, bytearray, or extensions like the NumPy arrays. Python
    variable-sized collections written in C include a struct2 called
    PyVarObject, which has an ob_size field holding the number of items in the
    collection. So, if my_object is an instance of one of those built-ins, then
    len(my_object) retrieves the value of the ob_size field, and this is much
    faster than calling a method.
    
    NOTE: Normally, your code should not have many direct calls to special
    methods. Unless y    - Why len() is not a method
ou are doing a lot of metaprogramming, you should be
    implementing special methods more often than invoking them explicitly.
    
    A pythonic Card Deck (project):
        this project is for implementing magic methods in classes 
        - namedtuple method
            collections.namedtuple is a factory function in the Python
            collections module that creates a subclass of tuple with named
            fields. It allows you to create lightweight, immutable data
            structures that are similar to tuples but provide named attributes
            for accessing the values.
            they are just classes with no methods, bundle of attributes
        
        Note: using list() will create a list of givin obj if give it a string
                it will convert each character of string in a item of list 
                
        magic methods in class:
            By implementing def __len__ in our project, we have changed the
            default behavior of len() and overridden it. same for __getitem__
            the behavior of obj[#] has changed by our needs.
            now that we implement __getitem__ in class, our deck automatically
            supports slicing and iteration
            
            Note: If a collection has no __contains__ method, the in operator
                does a sequential scan
        
        - random.choice:
            Python has a function to get a random item from a sequence 
            
- How to use Special methods
    by using special methods we can override default behaviour of language such
    as operators.

    Several special methods allow user objects to respond to operators 
    such as +.
    
    (Project) Vector Experiment:
        
        
    __abs__(): is absolute of value of integers and floats and the magnitude of
        complex numbers. (ghadr motlagh)
        Hypot() : moadele fisaghores
    
    __repr__() :
        The __repr__ special method is called by the repr built-in to get the
        string represenation of the object for inspection.
        Without a custom __repr__, Python’s console would display an Object
        instance <Object at 0x10e100070>.

        The string returned by __repr__ should be unambiguous and, if possible,
        match the source code necessary to re-create the represented object.
    
    __str__() :
        __str__ is called by the str() built-in and implicitly used by the
        print function. It should return a string suitable for display to end
        users.
        
    NOTE IMP: A basic requirement for a Python object is to provide usable
        string representations of itself, one used for debugging and logging,
        another for presentation to end users. That is why the special methods
        __repr__ and __str__ exist in the data model.
        
    NOTE: Sometimes same string returned by __repr__ is user-friendly, and you
        don’t need to code __str__ because the implementation inherited from
        the object class calls __repr__ as a fallback.
    
    NOTE: If you only implement one of these special methods in Python, choose
        __repr__.
        
    __bool__() :
        By default, instances of user-defined classes are considered truthy,
        unless either __bool__ or __len__ is implemented. Basically, bool(x)
        calls x.__bool__() and uses the result. If __bool__ is not implemented,
        Python tries to invoke x.__len__(), and if that returns zero, bool
        returns False. Otherwise bool returns True.

    INFIX OPERATOR: An infix operator is a type of operator used in programming
        and mathematics that is written between its operands. they create new
        objects without touching their operands.
        
- Collection API:
    ./python-collections.png
    The sequence, Mapping and set are abstracted from Collection ABC
    the collection itself is abstracted from three interfaces:
        Iterable(__iter__): Iterable to support for, unpacking, and other forms of
        iteration.
        
        Sized(__len__): Sized to support the len built-in function.
        
        Container(__contains__) : Container to support the "in" operator.
        
    NOTE: Only Sequence is Reversible, because sequences support arbitrary
        ordering of their contents, while mappings and sets do not.

- Why len() is not a method:
    No method is called for the built-in objects of CPython: the length is
    simply read from a field in a C struct.
    len is not called as a method because it gets special treatment as part of
    the Python Data Model
    
- What is python coding style?
    By implementing special methods, your objects can behave like the built-in
    types, enabling the expressive coding style the community considers
    Pythonic.

"""
