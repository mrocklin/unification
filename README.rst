Unification
===========

|Build Status|

Straightforward Unification, extensible via dispatch.

Examples
--------

.. code-block:: python

   >>> from unification import *
   >>> unify(1, 1)
   {}
   >>> unify(1, 2)
   False
   >>> x = var('x')

   >>> unify((1, x), (1, 2))
   {~x: 2}

   >>> unify((x, x), (1, 2))
   False

   @unifiable
   class Account(object):
       def __init__(self, id, name, balance):
           self.id = id
           self.name = name
           self.balance = balance

   data = [Account(1, 'Alice', 100),
           Account(2, 'Bob', 0),
           Account(2, 'Charlie', 0),
           Account(2, 'Denis', 400),
           Account(2, 'Edith', 500)]

   id, name, balance = var('id'), var('name'), var('balance')

   >>> [unify(Account(id, name, balance), acct) for acct in data]
   [{~name: 'Alice', ~balance: 100, ~id: 1},
    {~name: 'Bob', ~balance: 0, ~id: 2},
    {~name: 'Charlie', ~balance: 0, ~id: 2},
    {~name: 'Denis', ~balance: 400, ~id: 2},
    {~name: 'Edith', ~balance: 500, ~id: 2}]

   >>> [unify(Account(id, name, 0), acct) for acct in data]
   [False,
    {~name: 'Bob', ~id: 2},
    {~name: 'Charlie', ~id: 2},
    False,
    False]


History
-------

This was carved out from the LogPy_ project.

Author
------

`Matthew Rocklin`_


.. _LogPy: http://github.com/logpy/logpy/
.. _`Matthew Rocklin: http://matthewrocklin.com/
.. |Build Status| image:: https://travis-ci.org/mrocklin/unification.png
   :target: https://travis-ci.org/mrocklin/unification
