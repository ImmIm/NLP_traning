import pandas as pd


def get_stocks():
    df = pd.read_csv("data/stocks.tsv", sep='\t')
    symbols = df.Symbol.tolist()
    return symbols
    
def get_indexes():
    df = pd.read_csv("data/indexes.tsv", sep='\t')
    indexes = df.IndexName.tolist()
    return indexes


def get_companies():
    df = pd.read_csv("data/companies.csv", sep=',')
    companies = df.Name.tolist()
    return companies


def get_exchanges():
    df = pd.read_csv('data/stock_exchanges.tsv', sep='\t')
    exchanges = df.ISOMIC.tolist()+df["Google Prefix"].tolist()+df.Description.tolist()
    return exchanges


