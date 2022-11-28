# The mapping types provided by the standard library are all mutable.

# The types module provides a wrapper class called MappingProxyType, which,
# given a mapping, returns a mappingproxy instance that is a read-only but
# dynamic proxy for the original mapping. This means that updates to the
# original mapping can be seen in the mappingproxy, but changes cannot
# be made through it.

# lets build a MappingProxyType read-only mapping

from types import MappingProxyType

di = {1: 'A'}
di_proxy = MappingProxyType(di)  # so we made an immutable proxy

di[2] = "B"  # now di_proxy will change

print(di_proxy)
