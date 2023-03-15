#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2022.6.13
# Author :QinSidong

import pandas as pd

def SuperSample(input,step,output):
    df = pd.read_csv(input, header=None)
    len = df.shape[1]-2
    row = df.shape[0]

    for i in range(row):
        f = df.iloc[i:i+1]
        f_N = f.copy(deep=True)
        a = 0
        b = len
        n = b

        while a <= (n/2-11):
            f_N[a] = 'N'
            f_N[b] = 'N'
            if (a + 1) % int(step) == 0:
                df_temp = f_N.copy(deep=True)
                f = pd.concat([f, df_temp])
                
            a += 1
            b -= 1
        print(i)
        f.to_csv(output,mode='a',header=None,index=None)
        


#SuperSample('Sample.csv',10,'SSample.csv')


