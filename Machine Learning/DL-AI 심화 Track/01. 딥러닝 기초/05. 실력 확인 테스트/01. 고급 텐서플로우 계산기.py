import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def insert():
    
    x = float(input('정수 또는 실수를 입력하세요. x : '))
    y = float(input('정수 또는 실수를 입력하세요. y : '))
    z = float(input('정수 또는 실수를 입력하세요. z : '))
    cal = input('어떤 연산을 할 것인지 입력하세요. (+-, **, *+, /-)')
    
    return x, y, z, cal

# 지시사항 1번을 참고하여 코드를 작성하세요.
def calcul(x, y, z, cal):
    
    result = 0
    
    if cal == "+-":
        # +- 연산
        result = tf.subtract(tf.add(x, y), z)
    
    elif cal == "**":
        # ** 연산
        result = tf.multiply(tf.multiply(x, y), z)
    
    elif cal == "*+":
        # *+ 연산
        result = tf.add(tf.multiply(x, y), z)

    elif cal == "/-":   
        # /- 연산
        result = tf.subtract(tf.truediv(x, y), z)
    
    return result.numpy()
    
def main():
    
    x, y, z, cal = insert()
    
    print('\n연산 결과: ', calcul(x, y, z, cal))
    
if __name__ == "__main__":
    main()