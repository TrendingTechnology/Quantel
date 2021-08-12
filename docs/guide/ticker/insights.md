### **profile**

=== "Details"

    - *Description*:  Retrieves company profile
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.profile
    ```

=== "Data"

    ```python
    [{'address': '1600 Amphitheatre Parkway',
     'beta': 1.017391,
     'ceo': 'Mr. Sundar Pichai',
     'changes': -8.14,
     'cik': '0001652044',
     'city': 'Mountain View',
     'companyName': 'Alphabet Inc.',
     'country': 'US',
     'currency': 'USD',
     'cusip': '02079K107',
     'dcf': 2773.8,
     'dcfDiff': 376.88,
     'defaultImage': False,
     'description': 'Alphabet Inc. provides online advertising services in the '
                    'United States, Europe, the Middle East, Africa, the '
                    'Asia-Pacific, Canada, and Latin America. It offers '
                    'performance and brand advertising services. The company '
                    'operates through Google and Other Bets segments. The Google '
                    'segment offers products, such as Ads, Android, Chrome, Google '
                    'Cloud, Google Maps, Google Play, Hardware, Search, and '
                    'YouTube, as well as technical infrastructure. It also offers '
                    'digital content, cloud services, hardware devices, and other '
                    'miscellaneous products and services. The Other Bets segment '
                    'includes businesses, including Access, Calico, CapitalG, GV, '
                    'Verily, Waymo, and X, as well as Internet and television '
                    'services. The company has an agreement with Sabre Corporation '
                    'to develop an artificial intelligence-driven technology '
                    'platform for travel. Alphabet Inc. was founded in 1998 and is '
                    'headquartered in Mountain View, California.',
     'exchange': 'Nasdaq Global Select',
     'exchangeShortName': 'NASDAQ',
     'fullTimeEmployees': 139995,
     'industry': 'Internet Content & Information',
     'ipoDate': '2004-08-19',
     'isActivelyTrading': True,
     'isEtf': False,
     'isin': 'US02079K1079',
     'lastDiv': 0.0,
     'mktCap': 1827191914496.0,
     'phone': '650-253-0000',
     'price': 2753.79,
     'range': '1406.55-2800.22',
     'sector': 'Communication Services',
     'state': 'CA',
     'symbol': 'GOOG',
     'volAvg': 1136007,
     'website': 'http://www.abc.xyz',
     'zip': '94043'}]
    ```

### **analyst_estimates**

=== "Details"

    - *Description*:  Retrieves analyst estimates for key financial metrics
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.analyst_estimates
    ```

=== "Data"

    ```python
    [{'date': '2021-12-31',
     'estimatedEbitAvg': 39863199675,
     'estimatedEbitHigh': 40836481702,
     'estimatedEbitLow': 39437150662,
     'estimatedEbitdaAvg': 59980542854,
     'estimatedEbitdaHigh': 61445000921,
     'estimatedEbitdaLow': 59339484152,
     'estimatedEpsAvg': 63.9336,
     'estimatedEpsHigh': 75.705,
     'estimatedEpsLow': 52.9788,
     'estimatedNetIncomeAvg': 39993627601,
     'estimatedNetIncomeHigh': 40970094098,
     'estimatedNetIncomeLow': 39566184604,
     'estimatedRevenueAvg': 224762614999,
     'estimatedRevenueHigh': 234949860000,
     'estimatedRevenueLow': 206864140000,
     'estimatedSgaExpenseAvg': 32624449735,
     'estimatedSgaExpenseHigh': 33420993686,
     'estimatedSgaExpenseLow': 32275766872,
     'numberAnalystEstimatedRevenue': 35,
     'numberAnalystsEstimatedEps': 40,
     'symbol': 'GOOG'},
    ...
    ```
    
### **insider_transactions**

=== "Details"

    - *Description*:  Retrieves details of insider buying/selling
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.insider_transactions
    ```

=== "Data"

    ```python
    [{'currency': 'USD',
      'date': '2021-08-11',
      'orderType': 'Sell',
      'reportedName': 'Sergey Brin',
      'sharePrice': 2749.28,
      'shareVolume': 27739,
      'symbol': 'GOOG',
      'transactionValue': 76262884},
     {'currency': 'USD',
      'date': '2021-08-10',
      'orderType': 'Sell',
      'reportedName': 'Sergey Brin',
      'sharePrice': 2748.97,
      'shareVolume': 27787,
      'symbol': 'GOOG',
      'transactionValue': 76384923},
     {'currency': 'USD',
      'date': '2021-08-09',
      'orderType': 'Sell',
      'reportedName': 'L. John Hennessy',
      'sharePrice': 2741.42,
      'shareVolume': 199,
      'symbol': 'GOOG',
      'transactionValue': 546239},
     {'currency': 'USD',
      'date': '2021-08-09',
      'orderType': 'Sell',
      'reportedName': 'Sergey Brin',
      'sharePrice': 2736.64,
      'shareVolume': 27777,
      'symbol': 'GOOG',
      'transactionValue': 76016535},
     {'currency': 'USD',
      'date': '2021-08-04',
      'orderType': 'Sell',
      'reportedName': 'Sundar Pichai',
      'sharePrice': 2718.18,
      'shareVolume': 3000,
      'symbol': 'GOOG',
      'transactionValue': 8153625},
    ...
    ```
    
### **insider_transactions_summarized**

=== "Details"

    - *Description*:  Retrieves details of summarized insider buying/selling
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.insider_transactions_summarized
    ```

=== "Data"

    ```python
    [{'buyOrders': 0,
      'buyValue': 0,
      'buyVolume': 0,
      'currency': 'USD',
      'sellOrders': 117,
      'sellValue': 1815554556,
      'sellVolume': 817229,
      'symbol': 'GOOG'}]
    ```
    
### **share_ownership**

=== "Details"

    - *Description*:  Retrieves details of various shareholding groups
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.share_ownership
    ```

=== "Data"

    ```python
    [{'employeeShareScheme': 0,
      'firmsVCPE': 0,
      'generalPublic': 125002056,
      'hedgeFunds': 0,
      'individualInsiders': 83863092,
      'institutions': 457622262,
      'privateCompanies': 12522,
      'publicCompanies': 4718,
      'stateOrGovernment': 250254,
      'symbol': 'GOOG'}]

    ```

### **shares_float**

=== "Details"

    - *Description*:  Retrieves details of floating shares
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.shares_float
    ```

=== "Data"

    ```python
    [{'date': '2021-08-12',
      'floatShares': 580510157.0,
      'freeFloat': 179.4023601582298,
      'outstandingShares': 323580000.0,
      'source': 'https://www.sec.gov/ix?doc=/Archives/edgar/data/1652044/000165204421000047/goog-20210630.htm',
      'symbol': 'GOOG'}]
    ```
    
### **key_executives**

=== "Details"

    - *Description*:  Retrieves details of key company execs
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.key_executives
    ```

=== "Data"

    ```python
    [{'date': '2021-08-12',
      'floatShares': 580510157.0,
      'freeFloat': 179.4023601582298,
      'outstandingShares': 323580000.0,
      'source': 'https://www.sec.gov/ix?doc=/Archives/edgar/data/1652044/000165204421000047/goog-20210630.htm',
      'symbol': 'GOOG'}]
    ```