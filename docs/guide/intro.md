# Quantel - Intro

## Import Quantel

```python
from quantel import Quantel
```

## Authenticate API

Before we can pull information, we must instantiate the `Quantel` class and authenticate to the API

```python
qt = Quantel(api_key="<quantel-api-key>")
```

!!! note 
    Your API key will be validated during the Quantel class instantiation.

## Create Instance

To retrieve data from Quantel for a single stock, create an instance of the `ticker` class by passing the company's
ticker symbol as an argument:

```python
aapl = qt.ticker('aapl')
```

Or, pass in multiple symbols to retrieve data for multiple companies. Symbols can be passed in as a list:

```python
symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']
tickers = qt.ticker(symbols)
```

!!! note 
    Tickers parsed as uppercase or lowercase, it doesn't matter.

They can also be passed in as a string:

```python
symbols = 'FB AAPL AMZN NFLX GOOG'

tickers = qt.ticker(symbols)
```

!!! note 
    The Quantel API supports parsing multiple tickers (up to 30) to the same endpoint e.g. `https://quantel-io.p.rapidapi.com/profile/FB,AAPL,AMZN,NFLX,GOOG`.

    The Quantel Python library will handle this automatically. As such, the below code will only make one request to the API.  

For example:

```python
from quantel import Quantel

qt = Quantel(api_key="<quantel-api-key>")

symbols = 'fb aapl amzn nflx goog'

tickers = qt.ticker(symbols)

# Retrieve each company's profile information
data = tickers.profile
```

