
# TRADING PROGRAM 



# --  GOING TO USE ALL COMPONENTS W/N THIS FILE TO BUILD AN ALGO TRADER --

#IMPORT A BUNCH OF STUFF--

# import dotenv
from dotenv import load_dotenv
# import the operating system



import os

# this is how you get environmental variables
key = os.environ['key']
sec = os.environ['sec']


import datetime as dt
start_date = str(dt.datetime.now() + dt.timedelta(30))



import pandas as pd

import datetime
from statistics import mean
from datetime import date

import pandas as pd
import alpaca_trade_api as tradeapi
import time

from datetime import datetime
from pytz import timezone, utc
from urllib.error import HTTPError

date_format='%H:%M:%S'
date = datetime.now(tz=utc)
date = date.astimezone(timezone('US/Pacific'))
day=date.strftime("%D")




# ADD IN CHANGES BELOW THIS LINE:



previousclose = []
lastclose = []
buy_on_open = []
price_for_buy = []
buy_sell_hold = []
position_held = []
twentyavg = []
one_day_hold = []
sellable_pos = []
last_twenty_closes =[]


# MAKE SURE ACCOUNT IS WORKING: 

#API endpoint URL
url = "https://api.alpaca.markets"
#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')
#Init our account var
account = api.get_account()

print(account.status)
print(account.buying_power)
clock = api.get_clock()
portfolio = api.list_positions()
print("The market is open: {}".format(clock.is_open))




def run():
    
    from dotenv import load_dotenv
    # import the operating system
    import os
    
    # this is how you get environmental variables
    key = os.environ['key']
    sec = os.environ['sec']





    import pandas as pd
    import datetime
    from statistics import mean
    from datetime import date
    
    import pandas as pd
    import alpaca_trade_api as tradeapi
    import time
    from datetime import datetime
    from pytz import timezone, utc
    from urllib.error import HTTPError

    


    date_format='%H:%M:%S'
    date = datetime.now(tz=utc)
    date = date.astimezone(timezone('US/Pacific'))
    day=date.strftime("%D")

    previousclose = []
    lastclose = []
    buy_on_open = []
    price_for_buy = []
    buy_sell_hold = []
    position_held = []
    twentyavg = []
    one_day_hold = []
    sellable_pos = []
    last_twenty_closes =[]


    # MAKE SURE ACCOUNT IS WORKING: 

    #API endpoint URL
    url = "https://api.alpaca.markets"
    #api_version v2 refers to the version that we'll use
    #very important for the documentation
    api = tradeapi.REST(key, sec, url, api_version='v2')
    #Init our account var
    account = api.get_account()

    print(account.status)
    print(account.buying_power)
    clock = api.get_clock()
    portfolio = api.list_positions()
    print("The market is open: {}".format(clock.is_open))


    #Should print 'ACTIVE'
    def alpacaInfo():
        

        # MAKE SURE ACCOUNT IS WORKING: 

        #API endpoint URL
        url = "https://api.alpaca.markets"
        #api_version v2 refers to the version that we'll use
        #very important for the documentation
        api = tradeapi.REST(key, sec, url, api_version='v2')
        #Init our account var
        account = api.get_account()

        print(account.status)
        print(account.buying_power)
        clock = api.get_clock()
        portfolio = api.list_positions()
        print("The market is open: {}".format(clock.is_open))


    # SO AS NOT TO SPEND ALL YOUR MONEY
    money_to_spend = float(account.buying_power) * .75

    def update_lists(one_day_hold):
        # ADD PREVIOUS DAY LIST TO SELLABLE POSITIONS
        sellable_pos.extend(one_day_hold)
        for x in portfolio:
                if x.symbol not in sellable_pos:
                    sellable_pos.append(x.symbol)
        print("lists updated")
    # CLEAR PREVIOUS DAY LIST
        one_day_hold = []
        return one_day_hold
        

    # DAILY GET STOCKS WE ARE GOING TO BUY
    def getList():
        global buy_on_open
        buy_on_open = []
        payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        first_table = payload[0]
        second_table = payload[1]
        df = first_table
        symbols = df['Symbol'].values.tolist()
        c = 0
        sortedList = []
        # The loop to get the close information for each column
        for stock in symbols:
            c +=1
            
            try:
                last_twenty_closes =[]

                barset = api.get_barset(stock, 'day', limit=22)
                bars = barset[stock]

                yesterday_close = bars[-2]
                for bar in bars: 
                    last_twenty_closes.append(bar.c)
                #     print(bar.c)
                last_twenty_closes.pop( -1)
                last_twenty_closes.pop( -2)

                average_of_last_twenty = round(mean(last_twenty_closes),2)
                average_of_last_twenty

                # if close is less than 20 d rolling avg. and less than $101 per share
                if yesterday_close.c < average_of_last_twenty and yesterday_close.c < 101:

                    # MIGHT WANT TO KEEP STOCK IN PORTFOLIO OUT OF LIST
            
                    #################
                    buy_on_open.append((stock, yesterday_close.c))
                    #################

                else:
                    pass
                
                print(stock)
                print("{} of 500".format(c))
                if c == 250:
                    time.sleep(30)
                if c == 450:
                    time.sleep(15)
                print(len(buy_on_open))
            except KeyError:
                pass  
        time.sleep(10)
        return buy_on_open


            



    # CHECK FUNDS AND BUY WHAT WE CAN

    # If stock in portfolio already, avoid it


    def buyStocks():
        a=0
        #to buy things in list:
        #https://alpaca.markets/docs/api-documentation/how-to/orders/
        
        ###############
        # SORT THE STOCKS:
        sorted_List = []
        sorted_List = sorted(buy_on_open, key=lambda x: x[1])
        ################
        
        #BUY THEM: 
        #     money_to_spend = float(account.buying_power) * .75
        
        ###########################
        for symbol, lc in sorted_List: 
            a += 1
            
            

            # MAKE SURE ACCOUNT IS WORKING: 

            #API endpoint URL
            url = "https://api.alpaca.markets"
            #api_version v2 refers to the version that we'll use
            #very important for the documentation
            api = tradeapi.REST(key, sec, url, api_version='v2')
            #Init our account var
            account = api.get_account()

            print("Buying Power: ",account.buying_power)
            clock = api.get_clock()

            
            
            #########################
            print("{} of {}".format(a, len(sorted_List)))

            time.sleep(1)
            print("{}".format(symbol))
            if symbol not in sellable_pos:
                print("test2", symbol)
                
                print(float(account.buying_power), float(api.get_last_quote(symbol).askprice) )
                if float(api.get_last_quote(symbol).askprice) == 0 or api.get_last_quote(symbol).askprice == 0 or float(api.get_last_quote(symbol).askprice) == 0.0:
                    print("WHY IS THIS $0????")
                    pass
                elif float(account.buying_power) > (float(api.get_last_quote(symbol).askprice)+1) and float(api.get_last_quote(symbol).askprice) != 0:
                #buy one of each in the list
                    if float(account.buying_power) > (float(api.get_last_quote(symbol).askprice)+1) and float(account.buying_power) > lc:

                        try:
                            print("test3", symbol)
                            order = api.submit_order(symbol=((symbol)),
                                                qty = (1),
                                                side=("buy"),
                                                type="market",
                                                time_in_force="day")
                            time.sleep(5) #5 seconds
                            # money_to_spend = money_to_spend - float(api.get_last_quote(symbol).askprice)
                            one_day_hold.append(symbol)
                        except (HTTPError, APIError) as e:
                            print('APIError', symbol)
                            pass
                    else:
                        print("somehow got here, dont know how")
                    
                else:
                    print("test4", symbol)
                    print("not enough buying power")
                    if a > 20:
                        break
                    pass
            else: 
                pass
            
    # IF NEW DAY AND PRICE HAS GONE UP, SELL STOCKS, ELSE IF DOWN 14% BUY DOUBLE
    def sell_check():   

        print("Sell Check")
        for order in api.list_positions():
            if str(order.symbol) in sellable_pos:

                # UPDATE LAST VALUE ON LINE 245 FOR PROFIT YOU WANT
                if float(order.market_value) >= (float(order.avg_entry_price) * 1.02):
                    api.submit_order(symbol=((order.symbol)),
                                        qty = (int(order.qty)),
                                        side=("sell"),
                                        type="market",
                                        time_in_force="day")
                    sellable_pos.remove(order.symbol)
                    print("sold and removed")
                else: 
                    print("not high enough")
                    pass

                                                        
            #         elif str(order.symbol) in sellable_pos & order.market_value < order.avg_entry_price*.86        
            # #             IF HAVE ENOUGH BUYING POWER:
            #                 api.submit_order(symbol=((order.symbol)),
            #                      qty = ((OLD QTY * 2)),
            #                      side=("buy"),
            #                      type="market",
            #                      time_in_force="day"
                                
            else:
                pass
                                    
                                        

        

        # check a few times a day for price, while market is open...

    
    start_date = str(dt.datetime.now() + dt.timedelta(30))

    # print(start_date[:10])


    end_date = False
    if start_date == day:
            end_date = True
    ## WHILE DAY IS NOT EQUAL TO LIKE 2 WEEKS FROM NOW?
    while not end_date:
        
        print("starting")
        # time.sleep(60*60)
        
        date_format='%H:%M:%S'
        date = datetime.now(tz=utc)
        date = date.astimezone(timezone('US/Pacific'))
        day=date.strftime("%D")
    ##     MIGHT NEED TO RE CLEAR LISTS EVERY DAY??
        buy_on_open = []

        if start_date == day:
            end_date = True
        # NEED TO LOOP THIS, OTHERWISE PROGRAM WILL CLEAR ALL LISTS


        # # HOW THINGS SHOULD RUN: 

        # # IF MARKET OPEN:
    #     clear_output()
        alpacaInfo()
        day
        print(date)
        
        
        clock.is_open
        if clock.is_open:
            
    # KEEPS RUNNING when it shouldnt, this causes all the "daily" lists to mess up
    # need to make this happen once a day, by adding a second while loop
            
            # UPDATE PREVIOUS DAY TO SELLABLE (TO PREVENT DAY TRADING)                
            update_lists(one_day_hold)  

            # GET LIST OF NEW STOCKS TO BUY                    
            getList()
            print(buy_on_open)
            time.sleep(6)
            
            ## SORT LIST BY PRICE TO MAXIMIZE SHARES PURCHASED
            #sortList()

            # BUY NEW STOCKS (IF THEY ARE NOT ALREADY OWNED)
            buyStocks()
            
            print("run")
            print("one day hold:", one_day_hold)
            # SELL WHAT HAS GONE UP
            sell_check()
            

            # WHILE MARKET IS STILL OPEN SLEEP/SELL CHECK
            #CHECK AGAIN A FEW TIMES IF PRICES HAVE GONE UP
            clock.is_open
            while clock.is_open == True:
                account = api.get_account()
                clock = api.get_clock()
                portfolio = api.list_positions()
                print("The market is open: {}".format(clock.is_open))
                clock.is_open
                sell_check()
                print("waiting to check again")
                time.sleep(60*60)
                print('time now: {}'.format(date))


            # # CHECK TIME/MARKET HOURS/HAVE PROGRAM SLEEP UNTIL THE MORNING
            else: 
                print("The market is closed")
                for x in portfolio:
                    if x.symbol not in sellable_pos:
                        sellable_pos.append(x.symbol)
                print('added everything to sellable', sellable_pos)
                time.sleep(60*60)
                pass
            #continue???

        else:
            time.sleep(60*45)

    """
    OPTIONAL SETTINGS TO UPDATE:

    DATE TO RUN UNITL: LINE 278
    PERCENTAGE INCREASE TO SELL AT: LINE 245
    PRICE PER SHARE TO ADD TO LIST: LINE 128

    """                           
