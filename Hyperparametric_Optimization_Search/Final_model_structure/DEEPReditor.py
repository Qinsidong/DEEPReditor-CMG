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
def inputData(TrainData,TestData):
    Train = pd.read_csv(TrainData,header=None)
    Test = pd.read_csv(TestData,header=None)

    X_train, y_train = Train.iloc[:,:-1], Train.iloc[:,-1]
    X_test, y_test = Test.iloc[:,:-1], Test.iloc[:,-1]

    X_train = pd.get_dummies(X_train) #转one_hot
    X_test = pd.get_dummies(X_test)

    #数据不匹配
    # X_train = X_train.iloc[:-1,:]
    # X_test = X_test.iloc[:-1,:]
    # y_train = y_train.iloc[:-1]
    # y_test = y_test.iloc[:-1]

    X_train = X_train.values
    X_test = X_test.values
    y_train = y_train.values
    y_test = y_test.values

    print(len(X_train[2]))

    X_train = X_train.astype(np.float32)
    X_test = X_test.astype(np.float32)
    y_train = y_train.astype(np.float32)
    y_test = y_test.astype(np.float32)
    return X_train, X_test, y_train, y_test

a=[
   [16,16,16],
   [20,20,20],
   [22,22,22],
   [24,24,24],
   [26,26,26],
   [28,28,28],
   [30,30,30]
      ]

b = [

    [256,256,256],
    [256,128,256]
         ]



def modelHyper(model,best_epoch, X_train,y_train,X_test,y_test,n,hps):
    

    history = model.fit(X_train, y_train, epochs=best_epoch,batch_size=50, validation_split=0.2)

    eval_loss,eval_acc = model.evaluate(X_test, y_test)

    y_pred = model.predict(X_test,verbose=1)
    y_pred = np.around(y_pred,0).astype(int)
    pd.DataFrame(y_test.astype(int)).to_csv(f'y_test.csv',index=0,header=0)
    pd.DataFrame(y_pred).to_csv(f'y_pred{n}.csv',index=0,header=0)
    
    with open('result.txt','a') as file:
        print(eval_loss,eval_acc,hps,file=file)
    model.save(f'Model{n}.h5')

    return history

def figure(history,n):
    plt.plot(history.epoch, history.history.get('acc'),label='Train_ACC')
    plt.plot(history.epoch, history.history.get('val_acc'),label='Val_ACC')
    plt.plot(history.epoch, history.history.get('loss'),label='Train_loss')
    plt.plot(history.epoch, history.history.get('val_loss'),label='val_loss')

    plt.legend()
    plt.savefig(f'val{n}.jpg',dpi=300)
    plt.show()
    plt.close()




if __name__ == '__main__':
    def Start(path,lr,TrainData,TestData):
        if os.path.exists(path) == False :
            os.mkdir(path)
        os.chdir(path) 

        X_train, X_test, y_train, y_test = inputData(TrainData,TestData)
       
        
        for i in range(len(b)):
            b1= b[i][0]
            b2= b[i][1]
            b3= b[i][2]
            for j in range(len(a)):
                a1 = a[j][0]
                a2 = a[j][1]
                a3=  a[j][2]

                HPS=[a1,a2,a3,b1,b2,b3]
                model = tf.keras.Sequential([                                                                                           
                keras.layers.Embedding(2001,a1,input_length=2001),

                keras.layers.Conv1D(b1,a2,activation='relu',padding='same'),
                
                keras.layers.MaxPooling1D(),
                keras.layers.Conv1D(b2,a3,activation='relu',padding='same'),
                keras.layers.GlobalAveragePooling1D(),

                keras.layers.Dense(b3, activation='relu'),
                keras.layers.Dropout(rate=0.3,name='Dropout'),

                keras.layers.Dense(1,activation='sigmoid')

                ])   


                model.compile(optimizer=tf.keras.optimizers.Adam(lr = lr),
                            loss='binary_crossentropy',
                            metrics=['acc'])
                model.summary()
        
                n = i+1,j+1
        
                history=modelHyper(model,400, X_train,y_train,X_test,y_test,n,hps=HPS)
                
                
                #figure(history,n)
