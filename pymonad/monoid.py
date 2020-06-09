# --------------------------------------------------------
# (c) Copyright 2014, 2020 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------
""" Implements the base Monoid type.

A monoid is an algebraic structure consisting of a set of objects, S,
such as integers; strings; etc., and an operation usually denoted as
'+' which obeys the following rules:
  1. Closure: If 'a' and 'b' are in S, then 'a + b' is also in S.
  2. Identity: There exists an element in S (denoted 0) such that
     a + 0 = 0 + a = a
  3. Associativity: (a + b) + c = a + (b + c)

For monoid types, the '+' operation is implemented by the method
'mplus' and the static method 'mzero' is defined to return the
identity element of the type.

For example, integers can be monoids in two ways:
  1. mzero = 0 and mplus = addition
  2. mzero = 1 and mplus = multiplication

String can also form a monoid where mzero is the empty string and
mplus is concatenation.
"""

class _MonoidZero:
    def __add__(self, other):
        return other

    def __radd__(self, other):
        return other

    def __mul__(self, other):
        return other

    def __rmul__(self, other):
        return other

    def __repr__(self):
        return 'MZERO'

MONOID_ZERO = _MonoidZero()

class Monoid:
    """ Abstract base class for Monoid instances.

    To implement a monoid instance, users should create a sub-class of
    Monoid and implement the mzero and mplus methods. Additionally, it
    is the implementers responsibility to ensure that the
    implementation adheres to the closure, identity and associativity
    laws for monoids.
    """

    def __init__(self, value):
        """ Initializes the monoid element to 'value'.  """
        self.value = value

    def __add__(self, other):
        """ The 'mplus' operator.  """
        return self.mplus(other)

    def __eq__(self, other):
        return self.value == other.value


    @staticmethod
    def mzero():
        """
        A static method which simply returns the identity value for the monoid type.
        This method must be overridden in subclasses to create custom monoids.
        See also: the mzero function.

        """
        raise NotImplementedError

    def mplus(self, other):
        """
        The defining operation of the monoid. This method must be overridden in subclasses
        and should meet the following conditions.
           1. x + 0 == 0 + x == x
           2. (x + y) + z == x + (y + z) == x + y + z
        Where 'x', 'y', and 'z' are monoid values, '0' is the mzero (the identity value) and '+'
        is mplus.

        """
        raise NotImplementedError

def mzero(monoid_type):
    """
    Returns the identity value for monoid_type. Raises TypeError if
    monoid_type is not a valid monoid.

    There are a number of builtin types that can operate as monoids
    and they can be used as such as is. These "natural" monoids are:
    int, float, str, and list.  While thee mzero method will work on
    monoids derived from the Monoid class, this mzero function will
    work for *all* monoid types, including the "natural" monoids.  For
    this reason it is preferable to call this function rather than
    calling the mzero method directly unless you know for sure what
    type of monoid you're dealing with.

    """
    try:
        return monoid_type.mzero()
    except AttributeError:
        if (isinstance(monoid_type, (int, float)) or monoid_type == int or monoid_type == float): # pylint: disable=no-else-return
            return 0
        elif isinstance(monoid_type, str) or monoid_type == str:
            return ""
        elif isinstance(monoid_type, list) or monoid_type == list:
            return []
        else:
            raise TypeError(str(monoid_type) + " is not a Monoid.")

def mconcat(monoid_list):
    """
    Takes a list of monoid values and reduces them to a single value by applying the
    mplus operation to each all elements of the list.

    """
    result = mzero(monoid_list[0])
    for value in monoid_list:
        result += value
    return result
