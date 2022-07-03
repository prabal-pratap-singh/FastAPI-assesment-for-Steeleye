# FastAPI-assesment-for-Steeleye
This API was made as the  assessment work for steel eye.

# DATA SET
As per given assissment we are free to create  our own data set layer using pydant base model which is given to us as our data set foundation.
I have created data set as a list which consist of dictionaries beacause its is easy to access and manupulate data in a list, i.e: [{},{},{}...{}].
there are total 20 dictionary in our data set list which consist of 8 attributes and 3 sub attributes
each dictionary is called as trade and has its own attributes which are:
                |_ assetClass :   type str
                |_ counterparty :   type str
                |_ instrumentId :   type str
                |_ instrumentName :   type str
                |_ tradeDateTime :   type dt.datetime i.e, 2022-04-12T09:50:56
                |_ tradeDetails:
                          |_ buySellIndicator :   type str
                          |_ price :   type float
                          |_ quantity : type int
                |_ tardeId :   type str
                |_ tarder :   type str
Each attribute of an trade has some range of value which are predifine by me to use in test cases like sort, filtering etc.

