# Testing that tensorflow works
# Aki Sipovaara 2018

import tensorflow as tf

def main():
	hello = tf.constant('Hello!')
	sess = tf.Session()
	print(sess.run(hello))

main()
