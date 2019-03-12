# Introduction
Python wrapper for CEX.IO

# Installation
via pip

`pip install git+https://github.com/taxbit-open-source/python-cexio.git@master#egg=taxbit-cexio-python` 

# Getting started

```python
import taxbit_cexio

api = taxbit_cexio.Api('username', 'api_key', 'api_secret')

print(api.currency_limits)

```