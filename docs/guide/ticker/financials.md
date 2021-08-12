### **balance_sheet**

=== "Details"

    - *Description*:  Retrieves all balance sheet statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.balance_sheet
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'accountPayables': 5589000000,
     'accumulatedOtherComprehensiveIncomeLoss': 633000000,
     'cashAndCashEquivalents': 26465000000,
     'cashAndShortTermInvestments': 136694000000,
     'commonStock': 58510000000,
     'date': '2020-12-31',
     'deferredRevenue': 2543000000,
     'deferredRevenueNonCurrent': 481000000,
     'deferredTaxLiabilitiesNonCurrent': 3561000000,
     'fillingDate': '2021-02-03',
     'goodwill': 21175000000,
     'goodwillAndIntangibleAssets': 22620000000,
     'intangibleAssets': 1445000000,
     'inventory': 728000000,
     'longTermDebt': 13932000000,
     'longTermInvestments': 20703000000,
     'netDebt': 307000000,
     'netReceivables': 31384000000,
     'otherAssets': 0,
     'otherCurrentAssets': 5490000000,
     'otherCurrentLiabilities': 10409000000,
     'otherLiabilities': 0,
     'otherNonCurrentAssets': 3953000000,
     'otherNonCurrentLiabilities': 2269000000,
     'othertotalStockholdersEquity': 0,
     'period': 'FY',
     'propertyPlantEquipmentNet': 96960000000,
     'reportedCurrency': 'USD',
     'retainedEarnings': 163401000000,
     'shortTermDebt': 0,
     'shortTermInvestments': 110229000000,
     'symbol': 'GOOG',
     'taxAssets': 1084000000,
     'taxPayables': 1485000000,
     'totalAssets': 319616000000,
     'totalCurrentAssets': 174296000000,
     'totalCurrentLiabilities': 56834000000,
     'totalDebt': 26772000000,
     'totalInvestments': 130932000000,
     'totalLiabilities': 97072000000,
     'totalLiabilitiesAndStockholdersEquity': 319616000000,
     'totalNonCurrentAssets': 145320000000,
     'totalNonCurrentLiabilities': 40238000000,
     'totalStockholdersEquity': 222544000000
    },
    ...

    ```


### **balance_sheet_growth**

=== "Details"

    - *Description*:  Retrieves balance sheet growth by percentage data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.balance_sheet_growth
    ```

=== "Data"

    ```python
    [{'date': '2020-12-31',
     'growthAccountPayables': 0.005035065635677036,
     'growthAccumulatedOtherComprehensiveIncomeLoss': -1.5137987012987013,
     'growthCashAndCashEquivalents': 0.43069521029300467,
     'growthCashAndShortTermInvestments': 0.14221015249634428,
     'growthCommonStock': 0.15742206045260326,
     'growthDeferredRevenue': 0.3328092243186583,
     'growthDeferredRevenueNonCurrent': 0.3435754189944134,
     'growthDeferrredTaxLiabilitiesNonCurrent': 1.09347442680776,
     'growthGoodwill': 0.02671644685802948,
     'growthGoodwillAndIntangibleAssets': 0.000752112551431226,
     'growthIntangibleAssets': -0.269833249115715,
     'growthInventory': -0.27127127127127126,
     'growthLongTermDebt': 2.059288537549407,
     'growthLongTermInvestments': 0.5830402202171586,
     'growthNetDebt': -1.0220166379804934,
     'growthNetReceivables': 0.14156845627819,
     'growthOtherAssets': 0.0,
     'growthOtherCurrentAssets': 0.2443336355394379,
     'growthOtherCurrentLiabilities': -0.48257692498881544,
     'growthOtherLiabilities': 0.0,
     'growthOtherNonCurrentAssets': 0.29056480574600063,
     'growthOtherNonCurrentLiabilities': -0.9013092079509373,
     'growthOthertotalStockholdersEquity': -1.0,
     'growthPropertyPlantEquipmentNet': 0.1462754323950489,
     'growthRetainedEarnings': 0.07414443670212066,
     'growthShortTermDebt': 0.0,
     'growthShortTermInvestments': 0.08946697371932356,
     'growthTaxAssets': -0.3627278071722516,
     'growthTaxPayables': 4.41970802919708,
     'growthTotalAssets': 0.1584109253413263,
     'growthTotalCurrentAssets': 0.14234031118509877,
     'growthTotalCurrentLiabilities': 0.25680546648680924,
     'growthTotalDebt': 4.878787878787879,
     'growthTotalInvestments': 0.14596297755021662,
     'growthTotalLiabilities': 0.3035572804060859,
     'growthTotalLiabilitiesAndStockholdersEquity': 0.1584109253413263,
     'growthTotalNonCurrentAssets': 0.17829256229171903,
     'growthTotalNonCurrentLiabilities': 0.3758462695753265,
     'growthTotalStockholdersEquity': 0.10475471847976092,
     'period': 'FY',
     'symbol': 'GOOG'},
    ...

    ```

### **income_statement**

=== "Details"

    - *Description*:  Retrieves all income statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.income_statement
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'costAndExpenses': 141303000000,
     'costOfRevenue': 84732000000,
     'date': '2020-12-31',
     'depreciationAndAmortization': 13697000000,
     'ebitda': 54921000000,
     'ebitdaratio': 0.3008924707029645,
     'eps': 58.14692108710071,
     'epsdiluted': 58.14692108710071,
     'fillingDate': '2021-02-03',
     'generalAndAdministrativeExpenses': 11052000000,
     'grossProfit': 97795000000,
     'grossProfitRatio': 0.5357837470620785,
     'incomeBeforeTax': 48082000000,
     'incomeBeforeTaxRatio': 0.2634240413747007,
     'incomeTaxExpense': 7813000000,
     'interestExpense': 135000000,
     'netIncome': 40269000000,
     'netIncomeRatio': 0.22061941520980458,
     'operatingExpenses': 56571000000,
     'operatingIncome': 41224000000,
     'operatingIncomeRatio': 0.22585151785763202,
     'otherExpenses': 0,
     'period': 'FY',
     'reportedCurrency': 'USD',
     'researchAndDevelopmentExpenses': 27573000000,
     'revenue': 182527000000,
     'sellingAndMarketingExpenses': 17946000000,
     'sellingGeneralAndAdministrativeExpenses': 28998000000,
     'symbol': 'GOOG',
     'totalOtherIncomeExpensesNet': -6858000000,
     'weightedAverageShsOut': 675582000,
     'weightedAverageShsOutDil': 680794590},
    ...
    ```

### **income_statement_growth**

=== "Details"

    - *Description*:  Retrieves income statements growth by percentage data
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.income_statement_growth
    ```

=== "Data"

    ```python
    [{'date': '2020-12-31',
     'growthCostAndExpenses': 0.10716468431197405,
     'growthCostOfRevenue': 0.17853566262378992,
     'growthDepreciationAndAmortization': 0.16263475087004498,
     'growthEBITDA': 0.19362340259062852,
     'growthEBITDARatio': 0.05845328676366234,
     'growthEPS': 0.18274129580595216,
     'growthEPSDiluted': 0.18274129580595216,
     'growthGeneralAndAdministrativeExpenses': 0.1571563187100827,
     'growthGrossProfit': 0.08708218005580196,
     'growthGrossProfitRatio': -0.03602283269164575,
     'growthIncomeBeforeTax': 0.21342586750788645,
     'growthIncomeBeforeTaxRatio': 0.07601325084630736,
     'growthIncomeTaxExpense': 0.4791745550927679,
     'growthInterestExpense': 0.35,
     'growthNetIncome': 0.1725533587630667,
     'growthNetIncomeRatio': 0.03976928886857504,
     'growthOperatingExpenses': 0.04697129531952696,
     'growthOperatingIncome': 0.20428851041453652,
     'growthOperatingIncomeRatio': 0.06791064023495606,
     'growthOtherExpenses': -1.2309974045235448,
     'growthResearchAndDevelopmentExpenses': 0.059766315627642404,
     'growthRevenue': 0.12770532012826136,
     'growthSellingAndMarketingExpenses': -0.028054592720970536,
     'growthTotalOtherIncomeExpensesNet': -65.9113924050633,
     'growthWeightedAverageShsOut': -0.02448500727940423,
     'growthWeightedAverageShsOutDil': -0.01695822341614936,
     'period': 'FY',
     'symbol': 'GOOG'},
    ...
    ```

### **cash_flow**

=== "Details"

    - *Description*:  Retrieves all cash flow statements
    - *Return*:  `List[Dict]`

=== "Example"

    ```python
    from quantel import Quantel

    qt = Quantel(api_key="<your-quantel-api-key>")

    goog = qt.ticker('goog')
    goog.cash_flow
    ```

=== "Data"

    ```python
    [{'acceptedDate': '2021-02-02 20:12:25',
     'accountsPayables': 694000000,
     'accountsReceivables': -6524000000,
     'acquisitionsNet': -738000000,
     'capitalExpenditure': -22281000000,
     'cashAtBeginningOfPeriod': 18498000000,
     'cashAtEndOfPeriod': 26465000000,
     'changeInWorkingCapital': 1827000000,
     'commonStockIssued': 0,
     'commonStockRepurchased': -31149000000,
     'date': '2020-12-31',
     'debtRepayment': -2100000000,
     'deferredIncomeTax': 1390000000,
     'depreciationAndAmortization': 13697000000,
     'dividendsPaid': 0,
     'effectOfForexChangesOnCash': 24000000,
     'fillingDate': '2021-02-03',
     'freeCashFlow': 42843000000,
     'inventory': 0,
     'investmentsInPropertyPlantAndEquipment': -22281000000,
     'netCashProvidedByOperatingActivities': 65124000000,
     'netCashUsedForInvestingActivites': -32773000000,
     'netCashUsedProvidedByFinancingActivities': -24408000000,
     'netChangeInCash': 7967000000,
     'netIncome': 40269000000,
     'operatingCashFlow': 65124000000,
     'otherFinancingActivites': 2800000000,
     'otherInvestingActivites': 68000000,
     'otherNonCashItems': 1267000000,
     'otherWorkingCapital': 117462000000,
     'period': 'FY',
     'purchasesOfInvestments': -143751000000,
     'reportedCurrency': 'USD',
     'salesMaturitiesOfInvestments': 133929000000,
     'stockBasedCompensation': 12991000000,
     'symbol': 'GOOG'},
    ...
    ```