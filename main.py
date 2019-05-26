import tensorflow as tf
# https://habr.com/ru/post/326380/ & https://habr.com/ru/post/249215/ & https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/
import gensim
import pymorphy2

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
