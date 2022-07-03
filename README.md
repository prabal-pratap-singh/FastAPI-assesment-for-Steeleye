# FastAPI-assesment-for-Steeleye
This API was made as the  assessment work for steel eye.

# DATA SET
As per given assissment we are free to create  our own data set layer using pydant base model which is given to us as our data set foundation.  
I have created data set as a list which consist of dictionaries beacause its is easy to access and manupulate data in a list, i.e: [{},{},{}...{}].  
There are total 20 dictionary in our data set list which consist of 8 attributes and 3 sub attributes.  
Each dictionary is called as trade and has its own attributes which are: 

    - assetClass :   type str
    - counterparty :   type str
    - instrumentId :   type str
    - instrumentName :   type str
    - tradeDateTime :   type dt.datetime i.e, 2022-04-12T09:50:56
    - tradeDetails:
          - buySellIndicator :   type str
          - price :   type float
          - quantity : type int
    - tradeId :   type str
    - trader :   type str  
  
Each attribute of an trade has some range of value which are predifine by me to use in test cases like sort, filtering etc.  
The range of values are:  
( values are case sensitve so use them as given below )  
- assetClass          =  Equity, Commodities, Bond, Machinery, Real state  
- counterparty      =  prabal, zerodha, upstox, arpit, ananya, ananya enterprises, bhavya, ritesh  
- instrumentId      =  It is unique for every trade so, it start from a1 till a20  
- intrumentName     =  drums, guitar,, shares, loan, football, shares, plot, speaker, building, medical, house, sports car, rent, cars.  
- tradeDateTime     =  It is random for every trade and lowest is 2010-06-30T18:52:56 and highest is 2028-04-30T18:52:56  
- buySellIndicator  =  buy, sell.  
- price             =  It is also random and hence lowest is 10 and highest is 2000000  
- quantity          =  It is also random, lowest is 1 and highest is 1000  
- tradeId           =  It is unique for every tarde and start from t1 till t20  
- trader            =  ritesh, prabal, bob singh, ananya enterprises, arpit, LIC, zerodha, fcb, medical store, bhavya.

# CODE  

## Header file used:
``` python
import sys
from urllib import response
from fastapi import FastAPI, Path, Query
import datetime as dt
from datetime import *
from typing import Optional
from pydantic import BaseModel, Field
import json
```
