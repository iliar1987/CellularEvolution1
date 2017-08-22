# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:52:41 2017

@author: Iliya
"""

import tensorflow as tf

N = 30

M = 3

initCondition = tf.random_uniform((N,N),minval=-1,maxval=1,name='initCondition')

filt = tf.Variable(initial_value=tf.random_normal((M,M)))

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(filt.eval())
