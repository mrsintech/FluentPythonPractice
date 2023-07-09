"""
Bold subjects in this chapter:
    - Magic Methods
    - Emulating Numeric Types
    

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
    methods. Unless you are doing a lot of metaprogramming, you should be
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
            
- Emulating Numeric Types
    Several special methods allow user objects to respond to operators 
    such as +.
    
    (Project) Vector Experiment:
        A class to represent n Dimention vectors
        The built-in complex type can be used to represent twodimensional
        vectors, but our class can be extended to represent 
        n-dimensional vectors.
        
    

"""
