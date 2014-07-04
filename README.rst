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

Function Dispatch
-----------------

Unification supports function dispatch through pattern matching.


.. code-block:: python

   from unification.match import *

   n = var('n')
   @match(0)
   def fib(n):
       return 0

   @match(1)
   def fib(n):
       return 1

   @match(n)
   def fib(n):
       return fib(n - 1) + fib(n - 2)

   >>> map(fib, [0, 1, 2, 3, 4, 5, 6, 7, 8, 0])
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


This patten matching can be fairly complex

.. code-block:: python

   name, amount = var('name'), var('amount')

   @match({'status': 200, 'data': {'name': name, 'credit': amount}})
   def respond(name, amount):
       balance[name] +=  amount


   @match({'status': 200, 'data': {'name': name, 'debit': amount}})
   def respond(name, amount):
       balance[name] -= amount


   @match({'status': 404})
   def respond():
       print("Bad Request")


See full example in the examples directory.


History
-------

This was carved out from the LogPy_ and `Multiple Dispatch`_ projects.


Author
------

`Matthew Rocklin`_


.. _LogPy: http://github.com/logpy/logpy/
.. _`Multiple Dispatch`: http://github.com/mrocklin/multipledispatch/
.. _`Matthew Rocklin`: http://matthewrocklin.com/
.. |Build Status| image:: https://travis-ci.org/mrocklin/unification.png
   :target: https://travis-ci.org/mrocklin/unification
