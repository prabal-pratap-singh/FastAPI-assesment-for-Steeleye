# FastAPI-assesment-for-Steeleye
This API was made as the  assessment work for steel eye.

# DATA SET
As per given assissment we are free to create  our own data set layer using pydantic base model which is given to us as our data set foundation.  
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

Data is created in **JSON** file. 

# CODE  

## libraries  used:
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
All these libray are used as per as need in python code.  
## Pydantic Base model
Our data base is based on this pydantic base model which was provide by steeleye.
```python
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")
```  
## Importing Data set from JSON file
As we have created our data set in different file named as **data**, now we are calling it in our main code **FastAPI** and storing in  a list named as **data**.
```python
with open('data.json') as f: # import data from data.json file
    data= json.load(f)
```
## Calling FASTAPI
We are now call FastAPI in a varibale named as **app**.
```python
app=FastAPI()
```
## Adding new Trade in our data list
Here we our going to add new trade in our data set by using a **post** function in FastAPI, named as ** make_package** and then return our new data set in uvicorn website.
```python
@app.post('/Trade/') # add trade in data
async def make_package(trade: Trade):
    data.append(trade)
    return data
```
## Test1 - Listing trade
In this test case we have to return list of trade to the user
##approach
we will simply return the data set as it is already in a list
```python
@app.get("/listing-trades") # return all the trade
async def get_item():
        return data
 ```
## Test2 - Single trade
In this test the user will provide an input **trade_Id** to our FastAPI and then it will return the trade which has same trade_id.  
### approach
We will iterate through all the dictionary and in dictionary will we check if the attribute **trade_id** is equal to the given Id then we will return the Trade.  
if Trade_id didn't match with any trade then it will return Data not found.
```python
@app.get("/single-trade/{id}") # find single trade using its tardeId
async def get_item(id: str):
    for item in data:
        if item["trade_id"]==id:
            return item
 ```
## Test3 - Searching trades
In this test case the user will give us an input and we have to find if any trade that consist that word in them then we have to return the trade.  
We have to return all the trade that has that input in them.
The searching paarameter are:  

-counterparty
-instrumentId
-instrumentName
-trader
### approach
first I have created a new empty list with name as **data1** which will consist all the trade which has that input in them.  
Then I have started a loop to iterate through the trade and start comparing all searching parameter of every trade with the input.  
If the input matchs with the trade attributes then it will append in the empty list named as **data1**.  
And then finally return the **data1**.
```python
@app.get("/search/{search}") # search a specific word in all the trade and then return the trade if its matchs 
async def get_item(search: str):
    data1=[]

    for item in data:
        if item["counterparty"]==search:
            data1.append(item)
        elif item["instrumentId"]==search:
            data1.append(item)
        elif item["instrumentName"]==search:
            data1.append(item)
        elif item["trader"]==search:
            data1.append(item)
    return data1
```


