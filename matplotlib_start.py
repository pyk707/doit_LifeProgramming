#vscode에서 python 그래프가 안 보일 때 ↓
#https://geniekj.blogspot.com/2019/11/vscode-python.html


from matplotlib import pyplot as plt    #import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x)
plt.show(x)