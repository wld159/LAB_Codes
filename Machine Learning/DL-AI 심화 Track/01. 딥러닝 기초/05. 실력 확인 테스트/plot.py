import numpy as np
import matplotlib.pyplot as plt
import random

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def plot(x_test, y_test, predictions):
    
    rand_n = np.random.randint(100, size = 3)
    
    for i in rand_n:
        
        img = x_test[i].reshape(28,28)
        plt.imshow(img,cmap="gray")
        plt.show()
        plt.savefig("test.png")
        elice_utils.send_image("test.png")
        print("Label: ", y_test[i])
        print("Prediction: ", np.argmax(predictions[i]))