import numpy as np
import tensorflow as tf
from visual import *
from plotter import *
from dataloader import load_data

import logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

np.random.seed(100)
tf.random.set_seed(100)

'''
1. 입력층과 출력층은 그대로 사용합니다.
'''

def Develop():
    
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(256),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dense(128),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dropout(rate=0.3),
        tf.keras.layers.Dense(10, activation='softmax')
        ])
    
    return model
    
    
'''
2. 모델을 불러온 후 학습시키고 테스트 데이터에 대해 평가합니다.

   Step01. Develop 함수를 이용해 두 모델을 불러옵니다.
   
   Step02. 모델의 손실 함수, 최적화 알고리즘, 평가 방법을 설정합니다.
   
   Step03. 모델의 구조를 확인하는 코드를 작성합니다.
   
   Step04. 모델을 학습시킵니다. 두 모델 모두 'epochs'는 20,
           'batch_size'는 500으로 설정합니다. 검증용 데이터도 설정해주세요.
   
   Step05. 모델을 테스트하고 accuracy 점수를 출력합니다. 
           모델의 성능을 확인해보고, 목표값을 달성해보세요.
'''

def main():
    
    # Fashion-MNIST 데이터를 불러오고 전처리하는 부분입니다.
    (train_images, train_labels), (test_images, test_labels) = load_data()
    
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    
    develop_model = Develop()
    
    develop_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    develop_model.summary()
    
    history = develop_model.fit(train_images, train_labels, epochs=20, batch_size=500, validation_data=(test_images, test_labels), verbose=0)
    
    scores = develop_model.evaluate(test_images, test_labels)
    
    print('\naccuracy_develop: ', scores[-1])
    
    Visulaize([('Develop', history)])
    
    return history

if __name__ == "__main__":
    main()