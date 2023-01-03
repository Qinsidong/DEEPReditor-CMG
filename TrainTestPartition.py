#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2022.6.13
# Update :
# Author :QinSidong


import pandas as pd 

def TrainTest(Posfile,Negfile,n,random_state):
    Pos = pd.read_csv(Posfile, header=None)
    Neg = pd.read_csv(Negfile, header=None)   

    #随机打乱所有样本
    P = Pos.sample(frac=1.0)
    N = Neg.sample(frac=1.0)

    Train_P = P.sample(frac=0.8,replace=False, random_state=random_state)
    Test_P = P[~P.index.isin(Train_P.index)]

    Train_N = N.sample(frac=0.8,replace=False, random_state=random_state)
    Test_N = N[~N.index.isin(Train_N.index)]

    Train = pd.concat([Train_P,Train_N]).sample(frac=1.0, random_state=random_state)
    Test = pd.concat([Test_P,Test_N]).sample(frac=1.0, random_state=random_state)

    Train.to_csv(f"Train{n}.csv",header=0,index=0)
    Test.to_csv(f"Test{n}.csv",header=0,index=0)

