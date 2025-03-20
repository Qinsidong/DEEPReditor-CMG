#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2024.11.24
# Author :QinSidong
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def DNA_complement2(sequence):  #碱基互补配对
    trantab = str.maketrans('ACGTNacgt', 'TGCANTGCA')     # trantab = str.maketrans(intab, outtab)   # 制作翻译表
    string = sequence.translate(trantab)     # str.translate(trantab)  # 转换字符
    return string


def ExtractSeq(filenameFasta):          #提取序列数据
    with open(filenameFasta,'r') as x: #fasta文件
        dataInput = x.readlines()
        x.close()
    sequence = dataInput[1:]

    i=0
    seq0=str()                            #整理序列数据，转为List
    while i < len(sequence):
        seq0=seq0+str(sequence[i][0:-1])
        i=i+1
    seq=list(seq0)

    return seq
    
def getCID(FastaFile):
    seq = ExtractSeq(FastaFile)

    result = open('GC_ID_Sample.csv', 'w', encoding='gbk')   #########
    t= list(['ID']+list(range(1,502,1)))
    for j in range(0, len(t)-1):
        result.write(str(t[j]))
        result.write(',')
    result.write(str(t[-1]))
    result.write("\n")


    for i in range(250,len(seq)-250,1):
        if seq[i] == 'C':
            sample = list(seq[i-250:i+251])
            id = i+1
            l = [f'{id}']+sample
            for j in range(0, len(l)-1):
                result.write(str(l[j]))
                result.write(',')
            result.write(str(l[-1]))
            result.write("\n")
        else: 
            if seq[i] == 'G':
                sample = list(seq[i-250:i+251])
                id = i+1
                l = [f'{id}']+sample
                for h in range(0, len(l)-1):
                    result.write(str(DNA_complement2(l[h])))
                    result.write(',')
                result.write(str(DNA_complement2(l[-1])))
                result.write("\n")

    result.close()
    del seq

def modelMatch(Name):
    Genus = {'Cucurbita':0,'Nelumbo':1,'Citrullus':2,'Arabidopsis':13,'Lactuca':5,'Solanum':6,'Capsella':7,'Raphanus':8,'Brassica':9,'Oryza':10,'Triticum':11,'Zea':12}
    Family = {'Cucurbitaceae':14,'Nelumbonaceae':1,'Brassicaceae':15,'Asteraceae':5,'Solanaceae':6,'Poaceae':18}
    Order = {'Cucurbitales':14,'Proteales':1,'Brassicales':13,'Asterales':5,'Solanales':6,'Brassicales':16,'Rhoeadales':8,'Poales':18,}
    Class = {'Gunneridae':17,'Liliopsida':18}
   
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
    return model

def predict(model,threshold=0.9999):
    df = pd.read_csv('GC_ID_Sample.csv',header=None)      ###########
    df1 = df.iloc[1:,1:]
    df2 = pd.read_csv('.\\match\\append.csv',header=None) ################
    df2.columns = np.arange(1, 501 + 1)
    df3 = df1.append(df2, ignore_index=True)
    x = pd.get_dummies(df3)
    x = x.iloc[0:-4,:]

    ID = pd.DataFrame(df.iloc[1:,0])

    del df,df1,df2,df3

    preACC=model.predict(x,verbose=1)# 

    ID[1]=preACC 
    del model,preACC,x

    a = ID.drop(ID[ID[1]<threshold].index)
    a[0] = a[0].astype(str).astype(int)
    a[1] = a[1].astype(str).astype(float)
    ID[0] = ID[0].astype(str).astype(int)
    ID[1] = ID[1].astype(str).astype(float)
    ID=ID.rename(columns={0:"ID",
                    1:"PreACC"})
    ID.to_csv("allID_Pre.csv",index=False)
    a=a.rename(columns={0:"ID",
                    1:"PreACC"})
    a.to_csv('preEditingSites.csv',index=False)              #############

    plt.figure(figsize=(60,7))
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=24)
    plt.xlabel("Sequence length (bp)",fontsize=30)
    plt.ylabel("$\itACC$ ",fontsize=30)
    plt.scatter(a["ID"],a["PreACC"],s=400,c='green',alpha=0.3, cmap=None)
    plt.savefig("preEditingSites.png",dpi=600)                   ########
    plt.close()
    del ID,a

if __name__ == '__main__':
    def startWholeGen(FastaFile,Name,threshold=0.9999):
        getCID(FastaFile)
        model = modelMatch(Name)
        predict(model,threshold)


#model = modelMatch(['Gunneridae','Cucurbitales','Cucurbitaceae','Cucurbita'])
#predict(model,0.9999)
#startWholeGen("sequence (0).fasta",['Gunneridae','Cucurbitales','Cucurbitaceae','Cucurbita'],threshold=0.9999)




