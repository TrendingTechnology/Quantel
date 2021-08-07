<p align="center">
    <em>Official Python Library for the Quantel Finance API</em>
</p>
<p align="center">
    <a href="https://travis-ci.com/ratherbland/quantel" target="_blank">
        <img src="https://travis-ci.com/ratherbland/quantel.svg?branch=master" alt="Build Status">
    </a>
</p>

---

**Documentation**: <a target="_blank" href="https://quantel.io/docs">https://quantel.io/docs </a>

**Blog Posts**: WIP

**Website**: <a target="_blank" href="https://quantel.io">https://quantel.io </a>

---

## Overview

Some features of Quantel:

- **Fast**: Data is retrieved through API endpoints instead of web scraping. Additionally, asynchronous requests can be utilized with simple configuration
- **Simple**: Data for multiple symbols can be retrieved with simple one-liners
- **Lightweight**: Minimal reliance on third party packages
- **Powerful**: 40+ years of historical financial data for almost 25k thousand companies across the globe

## Requirements

Python 3.5+

- [Requests](https://requests.readthedocs.io/en/master/) - The elegant and simple HTTP library for Python, built for human beings.
- [Aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP Client/Server for asyncio and Python.

## Installation

```bash
pip install quantel
```

## Example

```python
from quantel import Quantel

qt = Quantel(api_key="<quantel-api-key>")

goog = qt.ticker('goog')

goog.profile
```

## Multiple Symbol Example

The `ticker` class also makes it easy to retrieve data for a list of symbols with the same API. Simply pass a list of symbols as the argument to the `ticker` class.

```python
from quantel import Quantel

qt = Quantel(api_key="<quantel-api-key>")

symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

faang = qt.ticker(symbols)

faang.profile
```

## Asynchronous Example

It really is that simple. Set `asynchronous=True` when instantiating the ticker class.

```python
from quantel import Quantel

qt = Quantel(api_key="<quantel-api-key>")

goog = qt.ticker('goog', asynchronous=True)

goog.profile
```

## License

This project is licensed under the terms of the MIT license.

---

Questions can be raised directly via <a href="mailto:guy@quantel.io">guy@quantel.io</a>