# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S_dU4U08q74TlJbbEWly9yN85lz2UWzJ
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.linspace(-5,5,5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, -x, '-r', label='A')
plt.plot(x, x+2, 'g', label='B')
plt.grid()
#plt.axis('equal')
plt.legend(loc='upper left')