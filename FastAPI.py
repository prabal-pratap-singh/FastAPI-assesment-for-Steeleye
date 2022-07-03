import string
import sys
from urllib import response
from fastapi import FastAPI, Path, Query
import datetime as dt
from datetime import *
from typing import Optional
from pydantic import BaseModel, Field
import json

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

app=FastAPI()


with open('data.json') as f:
    data= json.load(f)



@app.post('/Trade/')
async def make_package(trade: Trade):
    data.append(trade)
    return data

@app.get("/single-trade/{id}")
async def get_item(id: str):
    for item in data:
        if item["trade_id"]==id:
            return item

@app.get("/listing-trades")
async def get_item():
    for i in range(len(data)):
        return data

@app.get("/search/{search}")
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

@app.get("/advance-filtering")
async def get_item(*,assetClass:Optional[str]=None, end:Optional[dt.datetime]="3000-12-31T23:59:59", maxPrice: Optional[int]=sys.maxsize, minPrice: Optional[int]= -sys.maxsize-1, start: Optional[dt.datetime]="1900-12-31T23:59:59", tradeType: Optional[str]=None):
    data2=[]
    y=0
    start=str(start)
    arr=[1,2,3,4,5,6,7,8,9,0]
    for i in range(len(start)):
            if start[i] in arr:
                y=y*10+start[i]
    z=0
    end=str(end)
    for i in range(len(end)):
            if end[i] in arr:
                z=z*10+end[i]
    for trade in data:
        x=0
        string=str(trade["tradeDateTime"])
        for i in range(len(string)):
            if string[i] in arr:
                x=x*10+string[i]
        if assetClass == None:
            a_asset=trade["assetClass"]
        else:
            a_asset=assetClass
        if tradeType==None:
            a_trade=trade["tradeDetails"]["buySellIndicator"]
        else:
            a_trade=tradeType
        if trade["assetClass"]==a_asset and x>=y and x<=z and trade["tradeDetails"]["price"]<=maxPrice and trade["tradeDetails"]["price"]>=minPrice and trade["tradeDetails"]["buySellIndicator"]== a_trade:
            data2.append(trade)
    return data2

@app.get("/sorting")
async def get_item(*,parameter:str = Query(None, description="Sort by price or quantity"),type:str=Query(None,description="Ascending or Descending")):
    data3=[]
    if parameter=="price":
        for i in range(len(data)):
                trade=data[i]
                data3.append([trade["tradeDetails"]["price"],i])
        sorted_values=sorted(data3) # Sort the values
        # return sorted_values
        for i in range(len(sorted_values)):
            x=sorted_values[i][1]
            data3[i]=(data[x])
        if type=="ascending":
            return data3
        else:
            return data3[::-1]
    elif parameter=="quantity":
        for i in range(len(data)):
                trade=data[i]
                data3.append([trade["tradeDetails"]["quantity"],i])
        sorted_values=sorted(data3) # Sort the values
        # return sorted_values
        for i in range(len(sorted_values)):
            x=sorted_values[i][1]
            data3[i]=(data[x])
        if type=="ascending":
            return data3
        else:
            return data3[::-1]

@app.get("/pagination")
async def get_item(page_num:int = Query(1,description="Enter page number"), page_size: int = Query(1,description="Enter size of data in one page")):
    start = (page_num-1)*page_size
    end = start+page_size
    response={
        "data": data[start:end],
        "total": len(data),
        "count": page_size,
        "pagination":{
            "next": "next page",
            "previous": "previous page"
        }
    }

    if end>= len(data):
        response["pagination"]["next"]= None

        if page_num >1:
            response["pagination"]["previous"]=f"/pagination?page_num{page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"]= None
    else:
        if page_num>1:
            response["pagination"]["previous"]=f"/pagination?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"]=None

        response["pagination"]["next"]=f"/pagination?page_num={page_num+1}&page_size={page_size}"
    return response



        
