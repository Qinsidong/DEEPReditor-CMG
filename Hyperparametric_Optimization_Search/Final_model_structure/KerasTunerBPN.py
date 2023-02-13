#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time :2022.5.17
# Author :QinSidong

import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import kerastuner as kt
from sklearn.model_selection import train_test_split

np.set_printoptions(suppress=True) #小数不以科学计数法输出


data = pd.read_csv('Data.csv',header=None)

x, y = data.iloc[:,:-1], data.iloc[:-1,-1]
x = pd.get_dummies(x) #转one_hot
x=x.iloc[:-1,]
x = x.values
y= y.values

seqlen=len(x[2])

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=45)
X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)
y_train = y_train.astype(np.float32)
y_test = y_test.astype(np.float32)



#hp.Int('units', min_value=32, max_value=512, step=32)可以自己设定最大值和最小值及步长
#hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])自定义学习率

callbacks = [
    keras.callbacks.TensorBoard(log_dir='.\\rsult'), #log_dir将输出的日志保存在所要保存的路径中
    keras.callbacks.ModelCheckpoint('.\\rsult', save_best_only = True), 
    keras.callbacks.EarlyStopping(monitor='val_loss',patience=5, min_delta=1e-3),
]
stop_early = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5,min_delta=1e-3)]


# 构建模型，传入hp参数，使用其定义需要优化的参数范围，构成参数空间
def model_builder(hp):
    model = keras.Sequential() 
    hp_unit1 = hp.Int('unit1', min_value=32, max_value=512, step=32)
    model.add(keras.layers.Dense(units=hp_unit1, input_shape=(1002,),activation='relu')) #len(x[2])
    model.add(keras.layers.Dropout(rate=0.4))
    hp_unit2 = hp.Int('unit2', min_value=32, max_value=512, step=32)
    model.add(keras.layers.Dense(units=hp_unit2, activation='relu'))
    model.add(keras.layers.Dropout(rate=0.4))
    hp_unit3 = hp.Int('unit3', min_value=32, max_value=512, step=32)
    model.add(keras.layers.Dense(units=hp_unit3, activation='relu'))
    model.add(keras.layers.Dropout(rate=0.4))
    model.add(keras.layers.Dense(1,activation='sigmoid'))

    # Tune the learning rate for the optimizer
    # Choose an optimal value from 0.01, 0.001, or 0.0001
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp_learning_rate),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])  # accuracy，用于判断模型效果的函数
    return model

# kt.RandomSearch() https://keras.io/api/keras_tuner/tuners/random/ 
# kt.Hyperband() 《Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization》

tuner = kt.Hyperband(model_builder,
                         objective='val_accuracy',  # 优化的目标，验证集accuracy
                         max_epochs=100,            # 最大迭代次数
                         factor=3,
                         directory='my_dir',        # my_dir/intro_to_kt目录包含超参数搜索期间运行的详细日志和checkpoints
                         project_name='intro_to_kt')

#搜索最佳的超参数配置 tuner.results_summary()
tuner.search(X_train, y_train, epochs=150, validation_data=(X_test, y_test),
                 callbacks=stop_early)

best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

print(f"""
    ...................................The hyperparameter search is complete. The optimal number of units in the first densely-connected
    layers are {best_hps.get('unit1')} ,{best_hps.get('unit2')} ,{best_hps.get('unit3')} and the optimal learning rate for the optimizer
    is {best_hps.get('learning_rate')}...................................
    """)
model = tuner.hypermodel.build(best_hps)


  
history = model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))
model.save('model.h5')
#tiny_model.evaluate(X_train,y_train,batch_size=9,verbose=1)
#tiny_model.predict(X_test,batch_size=9,verbose=1)


plt.plot(history.epoch, history.history.get('accuracy'),label='Train_ACC')
plt.plot(history.epoch, history.history.get('val_accuracy'),label='Test_ACC')
plt.title('Test', fontsize=14)
plt.legend()

plt.savefig('test.jpg',dpi=300)
plt.show()

print(max(history.history.get('accuracy')))
print(max(history.history.get('val_accuracy')))

model = tf.keras.models.load_model('model.h5')

