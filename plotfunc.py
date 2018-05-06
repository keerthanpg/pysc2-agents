import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.show()
plt.xlabel('Episodes')
plt.ylabel('Reward')


f=open('scorelog', 'r')
X=[]
Y=[]
for line in f:
	line=line.split()
	X.append(int(line[0]))
	Y.append(float(line[1]))
	
plt.plot(X,Y)
plt.show() 
	