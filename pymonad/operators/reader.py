# --------------------------------------------------------
# (c) Copyright 2014, 2020 by Jason DeLaat.
# Licensed under BSD 3-clause licence.
# --------------------------------------------------------
""" Adds operators to the Reader monad. """
import pymonad.monad
import pymonad.operators.operators
import pymonad.reader

class _Reader(pymonad.operators.operators.MonadOperators, pymonad.reader._Reader): # pylint: disable=protected-access
    """ See pymonad.operators.operators and pymonad.reader. """

def Reader(function): # pylint: disable=invalid-name
    """ Creates an instance of the Reader monad.

    Args:
      function: a function which takes the read-only data as input and
        returns any appropriate type.

    Result:
      An instance of the Reader monad.
    """
    return _Reader(function, None)

Reader.apply = _Reader.apply
Reader.insert = _Reader.insert