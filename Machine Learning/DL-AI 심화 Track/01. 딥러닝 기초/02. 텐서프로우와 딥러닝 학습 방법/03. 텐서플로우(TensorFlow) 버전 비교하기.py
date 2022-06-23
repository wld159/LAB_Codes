import numpy as np
import logging, os

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


"""""
텐서플로우 1.x 버전
"""""

def tf1():
    
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    
    # 상수
    a = tf.constant(5)
    b = tf.constant(3)
    
    # 계산 정의
    add_op = a + b
    
    # 세션 시작
    sess = tf.Session()
    result_tf1 = sess.run(add_op)
    
    return a, b, result_tf1

"""""
텐서플로우 2.0 버전
"""""

def tf2():
    
    import tensorflow as tf
    tf.compat.v1.enable_v2_behavior()
    
    # 상수
    a = tf.constant(5)
    b = tf.constant(3)
    
    # 즉시 실행 연산
    result_tf2 = tf.add(a, b)
    
    return a, b, result_tf2.numpy()

def main():
    
    tf_2, tf_1 = tf2()[2], tf1()[2]
    
    print('result_tf1:', tf_1)
    print('result_tf2:', tf_2)
    
if __name__ == "__main__":
    main()