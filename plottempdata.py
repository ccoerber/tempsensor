import numpy as np
import matplotlib.pyplot as plt

plotdate = '241216'
roomname = 'recroom'

# get data from csv.  The CSV must be formatted properly!
x = np.fromfile(r"C:\Users\coerbc1\Desktop\241216_recroom_tempdata.csv", count=-1, sep=',')

#indices of max and min temperature values
minXix = x.argmin()
maxXix = x.argmax()

plt.plot(x)

# annotate minimum temperature
plt.annotate(r'Min temp=' + str(x.min()), xy=(minXix, x.min()), 
    xycoords='data', xytext=(-10, -30), textcoords='offset points', 
    fontsize=10, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    
# annotate max temperature
plt.annotate(r'Max temp=' + str(x.max()), xy=(maxXix, x.max()), 
    xycoords='data', xytext=(-10, +20), textcoords='offset points', 
    fontsize=10, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#plt.show()

fname = r"C:\Users\coerbc1\Python Scripts\tempsensor\tempsensor\\"
fname = fname + plotdate + '_' + roomname + '_tempdata.png'
plt.savefig(fname, dpi='figure')