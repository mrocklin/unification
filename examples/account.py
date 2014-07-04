from functools import partial
from collections import defaultdict
from unification import *
from unification.match import *

match = partial(match, Dispatcher=VarDispatcher)

balance = defaultdict(lambda: 0)

name, amount = var('name'), var('amount')

@match({'status': 200, 'data': {'name': name, 'credit': amount}})
def respond(name, amount):
    balance[name] +=amount


@match({'status': 200, 'data': {'name': name, 'debit': amount}})
def respond(name, amount):
    balance[name] -= amount


@match({'status': 404})
def respond():
    print("Bad Request")


if __name__ == '__main__':
    respond({'status': 200, 'data': {'name': 'Alice', 'credit': 100}})
    respond({'status': 200, 'data': {'name': 'Bob', 'debit': 100}})
    respond({'status': 404})
    print(dict(balance))
