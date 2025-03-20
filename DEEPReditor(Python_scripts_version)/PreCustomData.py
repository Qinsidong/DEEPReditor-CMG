#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2024.10.26
# Author :QinSidong
import tensorflow as tf
import pandas as pd


def start(Name,data,threshold=0.75):
    Genus = {'Cucurbita':0,'Nelumbo':1,'Citrullus':2,'Arabidopsis':13,'Lactuca':5,'Solanum':6,'Capsella':7,'Raphanus':8,'Brassica':9,'Oryza':10,'Triticum':11,'Zea':12}
    Family = {'Cucurbitaceae':14,'Nelumbonaceae':1,'Brassicaceae':15,'Asteraceae':5,'Solanaceae':6,'Poaceae':18}
    Order = {'Cucurbitales':14,'Proteales':1,'Brassicales':13,'Asterales':5,'Solanales':6,'Brassicales':16,'Rhoeadales':8,'Poales':18,}
    Class = {'Gunneridae':17,'Liliopsida':18}
    df = pd.read_csv(data,header=None)
    df2 = pd.read_csv('.\\match\\append.csv',header=None)
    df3=df.append(df2, ignore_index=True)
    x = pd.get_dummies(df3)
    x = x.iloc[0:-4,:]
    Input_Class,Input_Order,Input_Family,Input_Genus= Name[0],Name[1],Name[2],Name[3]
    if Input_Genus != 'None':
        model = tf.keras.models.load_model(f'.\\model\\Model{Genus[Input_Genus]}.h5')
    else:
        if Input_Family != 'None':
            model = tf.keras.models.load_model(f'.\\model\\Model{Family[Input_Family]}.h5')
        else:
            if Input_Order !='None':
                model = tf.keras.models.load_model(f'.\\model\\Model{Order[Input_Order]}.h5')
            else:
                model = tf.keras.models.load_model(f'.\\model\\Model{Class[Input_Class]}.h5')
    acc = model.predict(x)
    result = pd.DataFrame(acc)
    result.to_csv('preCustomSites.csv',header=None)
    Sample = len(result)
    PosNum = (result[result>=threshold].count())
    print(f"In total, {Sample} samples were predicted and {PosNum} were predicted as edited samples.") 
    return Sample,PosNum

#start(['Liliopsida','None','None','None'],'8Neg8Pos.csv',threshold=0.75)
