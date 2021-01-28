# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:55:35 2020

@author: Zor
"""

import urllib.request
import json
from time import sleep
from multiprocessing import Process
import sqlite3
import pandas as pd

conn = sqlite3.connect('my_db1.db')

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)\
                 Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': USER_AGENT}


def main_data():
    """Fetch fast data"""
    url = "http://ftx.com/api/futures"

    request = urllib.request.Request(url, None, headers)  # The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()  # The data u need
    dataj = json.loads(data)
    df = pd.DataFrame(dataj['result'])
    return df


def sub_data(df):
    """Fetch slow data"""
    names = df['name']

    result = []
    count = 0
    for name in names:

        url2 = 'https://ftx.com/api/futures/{}/stats'.format(name)
        request = urllib.request.Request(url2, None, headers)  # The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()  # The data u need
        dfs = json.loads(data)['result']
        dfs['name'] = name
        result.append(dfs)
        count += 1

        sleep(1)
    df1 = pd.DataFrame(result)
    df1.drop('name', axis=1, inplace=True)
    return df1


def calculate_bs(coin1, coin2):
    return (coin1['ask'] - coin2['bid']) / (coin1['ask']/2 + coin2['bid'] / 2)


def calculate_ss(coin1, coin2):
    return (coin1['bid'] - coin2['ask']) / (coin1['bid'] / 2 + coin2['ask'] / 2)


def make_combinations(df):
    name = []
    underlying = []
    extra_data = []

    for i in range(len(df)):
        description = df['description'][i]    # Get Description
        if ("Futures" in description or "Perpetual" in description) and "Hashrate" not in description:
            name.append(df['name'][i])
            underlying.append(df['underlying'][i])
            extra_data.append(
                {
                    'ask': df['ask'][i],
                    'bid': df['bid'][i]
                }
            )

    combinations = []
    for i in range(len(underlying)):
        j = i
        while j < len(underlying):
            if i != j:
                if underlying[i] == underlying[j]:
                    bs = calculate_bs(extra_data[i], extra_data[j])
                    ss = calculate_ss(extra_data[i], extra_data[j])
                    combination_tuple = (name[i], name[j], bs, ss)
                    if combination_tuple not in combinations:
                        combinations.append(combination_tuple)
            j += 1

    return pd.DataFrame(combinations, columns=['Pair A', 'Pair B', 'Buy Spread', 'Sell Spread'])


def first_time():
    print('the first_time')
    df = main_data()

    df1 = sub_data(df)
    df1 = df1.join(df1['greeks'].apply(pd.Series)).drop(columns=['greeks', 0])
    df1.drop('volume', inplace=True, axis=1)

    df2 = pd.concat([df, df1], axis=1)
    df2 = df2.fillna(0)
    df2.to_sql('futures_markets', con=conn, index=False, if_exists='replace')


MAIN_TIME = 5
SUB_TIME = 60 * 3


def save_main():
    while True:
        print('fetching fast data')
        sleep(MAIN_TIME)
        df = main_data()

        df2 = pd.read_sql_query('SELECT * from futures_markets', con=conn)
        df2[df.columns] = df
        df2 = df2.fillna(0)
        df2.to_sql('futures_markets', con=conn, index=False, if_exists='replace')

        df3 = make_combinations(df)
        df3 = df3.fillna(0)
        df3.to_sql('spreads', con=conn, index=False, if_exists='replace')


def save_sub():
    while True:
        print('fetching slow data')
        sleep(SUB_TIME)
        df = main_data()

        df1 = sub_data(df)
        df1.drop('volume', inplace=True, axis=1)
        df1 = df1.join(df1['greeks'].apply(pd.Series)).drop(columns=['greeks', 0])

        df2 = pd.concat([df, df1], axis=1)
        df2 = df2.fillna(0)
        df2.to_sql('futures_markets', con=conn, index=False, if_exists='replace')
        print('fetching slow data finished')


if __name__ == '__main__':
    first_time()
    while True:
        q = Process(target=save_main)
        q.start()
        s = Process(target=save_sub)
        s.start()
        q.join()
        s.join


# (every 1 min)
# get futures markets data, save to db
# for each future: get stats, merge with basic data in db
# create combinations, calculate spreads, save to db
