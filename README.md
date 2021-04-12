[![lambdas logo](https://raw.githubusercontent.com/dry-python/brand/master/logo/lambdas.png)](https://github.com/dry-python/lambdas)

-----

[![Build Status](https://github.com/dry-python/lambdas/workflows/test/badge.svg?branch=master&event=push)](https://github.com/dry-python/lambdas/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/dry-python/lambdas/branch/master/graph/badge.svg)](https://codecov.io/gh/dry-python/lambdas)
[![Documentation Status](https://readthedocs.org/projects/lambdas/badge/?version=latest)](https://lambdas.readthedocs.io/en/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/lambdas.svg)](https://pypi.org/project/lambdas/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Telegram chat](https://img.shields.io/badge/chat-join-blue?logo=telegram)](https://t.me/drypython)

-----

Write short and fully-typed `lambda`s where you need them.


## Features

- Allows to write `lambda`s as `_`
- Fully typed with annotations and checked with `mypy`, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)
- Has a bunch of helpers for better composition
- Easy to start: has lots of docs, tests, and tutorials


## Installation

```bash
pip install lambdas
```

You also need to configure `mypy` correctly and install our plugin:

```ini
# In setup.cfg or mypy.ini:
[mypy]
plugins =
  lambdas.contrib.mypy.lambdas_plugin
```

We recommend to use the same `mypy` settings [we use](https://github.com/wemake-services/wemake-python-styleguide/blob/master/styles/mypy.toml).


## Examples

Imagine that you need to sort an array of dictionaries like so:

```python
>>> scores = [
...     {'name': 'Nikita', 'score': 2},
...     {'name': 'Oleg', 'score': 1},
...     {'name': 'Pavel', 'score': 4},
... ]

>>> print(sorted(scores, key=lambda item: item['score']))
[{'name': 'Oleg', 'score': 1}, {'name': 'Nikita', 'score': 2}, {'name': 'Pavel', 'score': 4}]
```

And it works perfectly fine.
Except, that you have to do a lot of typing for such a simple operation.

That's where `lambdas` helper steps in:

```python
>>> from lambdas import _

>>> scores = [
...     {'name': 'Nikita', 'score': 2},
...     {'name': 'Oleg', 'score': 1},
...     {'name': 'Pavel', 'score': 4},
... ]

>>> print(sorted(scores, key=_['score']))
[{'name': 'Oleg', 'score': 1}, {'name': 'Nikita', 'score': 2}, {'name': 'Pavel', 'score': 4}]
```

It might really save you a lot of effort,
when you use a lot of `lambda` functions.
Like when using [`returns`](https://github.com/dry-python/returns) library.

We can easily create math expressions:

```python
>>> from lambdas import _

>>> math_expression = _ * 2 + 1
>>> print(math_expression(10))
21
>>> complex_math_expression = 50 / (_ ** 2) * 2
>>> print(complex_math_expression(5))
100.0
```

Work in progress:

- `_.method()` is not supported yet for the same reason
- `TypedDict`s are not tested with `__getitem__`
- `__getitem__` does not work with list and tuples (collections), only dicts (mappings)

For now you will have to use regular `lamdba`s in these cases.
