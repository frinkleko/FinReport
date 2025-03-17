# FinReport: Explainable Stock Earnings Forecasting via News Factor Analyzing Model
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/finreport-explainable-stock-earnings/stock-market-prediction-on-astock)](https://paperswithcode.com/sota/stock-market-prediction-on-astock?p=finreport-explainable-stock-earnings)

PyTorch implementation for [WWW'2024] ["FinReport: Explainable Stock Earnings Forecasting via News Factor Analyzing Model"](https://arxiv.org/abs/2403.02647)

![Framework](imgs/framework.png)

## ​Important Notice​  
This repository contains a ​**demonstration version**​ of the code and data, designed to help readers understand the model architecture and workflow. Due to commercial agreements and technical confidentiality constraints after the publication of the paper, we are unable to open-source the full implementation or the complete dataset used in the experiments. The provided code and data are for illustrative purposes only and ​do not represent the actual implementation or dataset used in the paper.  

## Example Reports
![Example Reports](imgs/report.png)

## Obtaining Factors
There are two ways to get the factors:

### First Way
The first way relies on the `stockstats` library, which is a wrapper for pandas dataframes. 
```bash
pip install stockstats
```
Commonly you can input a pandas dataframe with the following columns: `['date', 'open', 'close', 'high', 'low', 'volume']`to use the `wrap` function to get the factors. 
```python
import pandas as pd
from stockstats import wrap

data = pd.read_csv('stock.csv')
df = wrap(data)
```
Check the [documentation for stockstats](https://github.com/jealous/stockstats) for more details.
More details and examples can also be found in [`src/Tech_Indicators.py`](./src/Tech_Indicators.py).

### Second Way
The second way to obtain the factors is to API from platforms like IFind, which provides a variety of factors. We recommend using this method to obtain more factors more esaily.

Codes are available in [`src/IFind_Indicators.py`](./src/IFind_Indicators.py). You can run it after filling the `access_token` in Line 10, customizing necessary parameters of `form_data` in Line 14.
