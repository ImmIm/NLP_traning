from stocksParse import get_companies, get_exchanges, get_indexes, get_stocks


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_patterns():
    patterns = []
    companies_false_positive_stops = ['two']

    for symbol in get_stocks():
        patterns.append({"label" : 'STOCK', "pattern": symbol, "UPPER" : True})
        patterns.append({"label" : 'STOCK', "pattern": f'.'+symbol, "UPPER" : True})
        for l in letters:
            patterns.append({"label": "STOCK", "pattern": symbol+f'.{l}'})

    
    for index in get_indexes():
        patterns.append({"label" : 'INDEX', "pattern": index})
        words = index.split()
        patterns.append({"label" : 'INDEX', "pattern": " ".join(words[:2])})
            
    for company in get_companies():
        if company not in companies_false_positive_stops:
            patterns.append({"label" : 'COMPANY', "pattern": company})
        
        
    for exchange in get_exchanges():
        patterns.append({"label": "STOCK_EXANGE", "pattern" : exchange})
    
    
    return patterns