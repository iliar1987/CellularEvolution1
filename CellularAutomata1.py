# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:42:21 2017

@author: Iliya
"""

import numpy as np
import scipy as sp
from scipy.signal import convolve2d
from matplotlib import pyplot as plt
import matplotlib as mpl

N = 50



outerTotalisticFilt = np.array([[1,1,1],[1,0,1],[1,1,1]],dtype=int)

states = 2

board = np.random.randint(low=0,high=states,size=(N,N))

totalValueOptions = (outerTotalisticFilt.sum()+1) * (states-1)

ruleRandom = np.random.randint(low=0,high=states,size=(totalValueOptions,states))
ruleLife = np.array([[0,0,0,1,0,0,0,0,0],
                     [0,0,1,1,0,0,0,0,0]], dtype=int).transpose()

def FilterStepCont(board,rule,filt):
    values = convolve2d(board,filt,mode='same',boundary='wrap')
    result = rule[values,board]
    return result

from PyQt5 import QtGui,QtCore,QtWidgets

fig = plt.figure()

def AdvanceOneFrame():
    global board
    board = FilterStepCont(board,ruleRandom,outerTotalisticFilt)
    imageBoard.set_data(board)
    plt.draw()

qtimer = None
def Start():
    global qtimer
    if qtimer is not None:
        qtimer.stop()
        qtimer = None
        return
    qtimer = QtCore.QTimer()
    qtimer.setInterval(50)
    qtimer.setSingleShot(False)
    qtimer.timeout.connect(AdvanceOneFrame)
    qtimer.start()


act = QtWidgets.QAction('play',None)

act.triggered.connect(Start)
fig.canvas.toolbar.addAction(act)
cmap = mpl.cm.get_cmap('jet')

imageBoard = plt.imshow(board,cmap=cmap)
