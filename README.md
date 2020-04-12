# clapsolver

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://github.com/jdmoorman/clapsolver/workflows/Build%20Master/badge.svg)](https://github.com/jdmoorman/clapsolver/actions)
[![Code Coverage](https://codecov.io/gh/jdmoorman/clapsolver/branch/master/graph/badge.svg)](https://codecov.io/gh/jdmoorman/clapsolver)

Fast constrained linear assignment problem (CLAP) solvers for Python

---

## Installation
**Stable Release:** `pip install clapsolver`<br>
**Development Head:** `pip install git+https://github.com/jdmoorman/clapsolver.git`

## Quick Start

Import the the `clap` module from the package and define your cost matrix.

```python
>>> from clapsolver import clap
>>> costs = [[0, 0, 1],
...          [1, 0, 2]]

```

Solve the linear assignment problem with row 0 forcibly assigned to column 1.

```python
>>> clap.cost(0, 1, costs)
1

```

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.
