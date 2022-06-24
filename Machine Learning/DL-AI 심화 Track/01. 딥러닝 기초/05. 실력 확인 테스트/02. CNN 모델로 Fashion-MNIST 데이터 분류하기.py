import tensorflow as tf
import numpy as np
import random
import os
from plot import *
import warnings, logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# 채점을 위한 코드입니다. 수정하지 마세요!
np.random.seed(81)
tf.random.set_seed(81)

def CNN():
    
    # 지시사항 1번을 참고하여 코드를 작성하세요. 
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(filters=8, kernel_size=(3, 3), strides=(1, 1), padding='SAME', input_shape=(28, 28, 1)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=(5, 5), strides=(1, 1), padding='SAME', input_shape=(28, 28, 1)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(filters=24, kernel_size=(3, 3), strides=(1, 1), padding='SAME', input_shape=(28, 28, 1)))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Activation('relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    
    return model
    
def main():
    
    # 데이터를 불러옵니다.
    x_train = np.loadtxt('./data/train_images.csv', delimiter =',', dtype = np.float32)
    y_train = np.loadtxt('./data/train_labels.csv', delimiter =',', dtype = np.float32)
    x_test = np.loadtxt('./data/test_images.csv', delimiter =',', dtype = np.float32)
    y_test = np.loadtxt('./data/test_labels.csv', delimiter =',', dtype = np.float32)
    
    # 지시사항 2번을 참고하여 코드를 작성하세요.
    num_train = 4000
    num_test = 1000
    width = 28
    height = 28
    num_channel = 1

    x_train = x_train.reshape((num_train, width, height, num_channel))
    x_test = x_test.reshape((num_test, width, height, num_channel))
    
    model = CNN()
    
    # 지시사항 3번을 참고하여 코드를 작성하세요. 
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
                  
    # 지시사항 4번을 참고하여 코드를 작성하세요. 
    history = model.fit(x_train, y_train, epochs=10, batch_size=64, verbose=2)
    
    # 지시사항 5번을 참고하여 코드를 작성하세요. 
    loss, test_acc = model.evaluate(x_test, y_test)
    predictions = model.predict(x_test)
    
    print('\nTEST 정확도 :', test_acc, '\n')
    
    # 완성된 모델을 확인해봅니다.
    model.summary()
    
    # 임의의 3가지 test data의 이미지와 실제 레이블 값을 출력하고 예측된 레이블 값을 출력합니다.
    plot(x_test, y_test, predictions)
    
if __name__ == "__main__":
    main()