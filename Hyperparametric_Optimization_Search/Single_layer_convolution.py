#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2022.5.17
# Author :QinSidong

import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

import os

#划分好的
def inputData(TrainData):
    Train = pd.read_csv(TrainData,header=None)
    X_train, y_train = Train.iloc[:,:-1], Train.iloc[:,-1]

    X_train = pd.get_dummies(X_train) #转one_hot

    X_train = X_train.values
    y_train = y_train.values

    X_train = X_train.astype(np.float32)

    y_train = y_train.astype(np.float32)

    return X_train, y_train



a=[
    [10,10],
    [12,12],
    [14,14],
    [16,16],
    [18,18],
    [20,20],
    [22,22],
    [24,24],
    [26,26]
      ]

b = [
        [32,64],
        [32,128],
        [32,256],
        [64,32],
        [64,64],
        [64,128],
        [64,256],
        [128,32],
        [128,64],
        [128,128],
        [128,256],
        [256,32],
        [256,64],
        [256,128],
        [256,256]
         ]




def modelHyper(model,best_epoch, X_train,y_train,n,hps):
    
    history = model.fit(X_train, y_train, epochs=best_epoch,batch_size=50,verbose=2, validation_split=0.2)
    trainACC = history.history.get('acc')
    valACC = history.history.get('val_acc')
    trainLoss = history.history.get('loss')
    valLoss = history.history.get('val_loss')
    maxTrainACC = max(trainACC)
    maxValACC = max(valACC)
    maxTrainLoss = max(trainLoss)
    maxValLoss = max(valLoss)

    with open('result.txt','a') as file:
        print(maxTrainACC,maxValACC,maxTrainLoss,maxValLoss,trainACC[-1],valACC[-1],trainLoss[-1],valLoss[-1],hps,file=file)

    return history

def figure(history,n):
    plt.plot(history.epoch, history.history.get('acc'),label='Train_ACC')
    plt.plot(history.epoch, history.history.get('val_acc'),label='Val_ACC')
    plt.plot(history.epoch, history.history.get('loss'),label='loss')
    plt.plot(history.epoch, history.history.get('val_loss'),label='val_loss')
    plt.legend()
    plt.savefig(f'val{n}.jpg',dpi=300)
    plt.show()



if __name__ == '__main__':
    def Start(path,lr,TrainData,n):
        if os.path.exists(path) == False :
            os.mkdir(path)
        os.chdir(path) 
        with open('result.txt','a') as file:
            print('maxTrainACC','maxValACC','maxTrainLoss','maxValLoss','trainACC','valACC','trainLoss','valLoss','hps',file=file)

        X_train,y_train = inputData(TrainData)
        
        for i in range(len(a)):
            a1= a[i][0]
            a2= a[i][1]

            for j in range(len(b)):
                b1 = b[j][0]
                b2 = b[j][1]

                HPS=[a1,a2,b1,b2]
                model = tf.keras.Sequential([                                                                                           
                keras.layers.Embedding(2001,a1,input_length=2001),

                keras.layers.Conv1D(b1,a2,activation='relu',padding='same'),
                
                # keras.layers.MaxPooling1D(),
                # keras.layers.Conv1D(b2,a3,activation='relu',padding='same'),
                keras.layers.GlobalAveragePooling1D(),

                keras.layers.Dense(b2, activation='relu'),

                keras.layers.Dense(1,activation='sigmoid')

                ])   

                model.compile(optimizer=tf.keras.optimizers.Adam(lr = lr),
                            loss='binary_crossentropy',
                            metrics=['acc'])
                model.summary()
        
        
        
                history=modelHyper(model,300, X_train,y_train,n,hps=HPS)
                
                c= [i,j]
                figure(history,c)
                

#Start('.\\LR0.01_50_10',0.01,'Train0.csv',0)
