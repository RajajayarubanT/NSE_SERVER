#imports
from pynse import *
from datetime import datetime
import json

#config logging
# nse
nse = Nse()



def findresult(symbol, query, start, end, expiry) :
    
    if symbol and query :
        
        if query == 'historical' :
            data = getHistorical_data(symbol, start, end)
            return data
            
        elif query == 'informations' :
            data = getInformation(symbol)
            return data
        elif query == 'quote' :
            data = getQuotes(symbol)
            return data
        elif query == 'option_chain' :
            if expiry : 
                data = getOption_chain(symbol, expiry)
                return data
            else : 
                data = getOption_chain(symbol, 0)
                return data
                
    if not(symbol) and query :
        
        if query == 'market_status' :
            getMarket_Status()
        elif query == 'expiry_strike_list' :
            getExpiry_Strike_list()


# data functions
def getMarket_Status():
    
    return  nse.market_status()
    
def getExpiry_Strike_list():
    
    expiry_list = nse.expiry_list
    strike_list = nse.strike_list
    
    return [expiry_list, strike_list]
    
def getOption_chain(symbol, expiry):
    
    if symbol :
        
        if expiry != 0 : 
            
            data = nse.option_chain(symbol,expiry)
            data = json.dumps(json.loads(data.to_json(orient='index')), indent=2)
            return  data
        else : 
            data = nse.option_chain(symbol)
            data = json.dumps(json.loads(data.to_json(orient='index')), indent=2)
            return  data
    
def getQuotes(symbol):
    
    if symbol :
        data = nse.get_quote(symbol)
        timeStamp = data['timestamp'].strftime("%y-%m-%d %H:%M:%S")        
        dt = datetime.strptime(timeStamp, '%y-%m-%d %H:%M:%S')
        ms = dt.timestamp() * 1000
        data['timestamp'] = ms
        data = json.dumps(data, indent = 4) 
        return  data
    
def getInformation(symbol):
    
    if symbol :
        
        return  nse.info(symbol)
    
def getHistorical_data(symbol, start, end):
    
    if symbol and start and end:
       
        _start = datetime.fromtimestamp(int(start)/1000.0)
        _end = datetime.fromtimestamp(int(end)/1000.0)
        data = nse.get_hist(symbol, _start, _end)
        
        data = json.dumps(json.loads(data.to_json(orient='index')), indent=2)

            
        return data