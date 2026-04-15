# DQMC

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/drazerd/dqmc)
![GitHub license](https://img.shields.io/github/license/drazerd/dqmc)

Efficient and stable Determinant Quantum Monte Carlo (DQMC) simulations of the Hubbard model in Python.

| :warning: WARNING: This project is still under active development and may change significantly in future versions! |
|--------------------------------------------------------------------------------------------------------------------|

| ℹ️ This version uses a pure Python + Numba backend. Fortran acceleration has been removed for simpler installation and maintenance. |

---

## Features

- Pure Python implementation
- Numba JIT acceleration
- Stable ASvQRD matrix stabilization
- Determinant Quantum Monte Carlo for Hubbard model
- Multiprocessing support
- Equal-time observable measurements

---

## Installation

Install directly from GitHub:

```commandline
pip install git+https://github.com/drazerd/dqmc.git