import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.show()
plt.xlabel('Episodes')
plt.ylabel('Reward')


f=open('log_loop', 'r')
X=[]
Y=[]
Y_err=[]
for line in f:
	line=line.split()
	X.append(int(line[0])-97000)
	Y.append(float(line[1]))
	Y_err.append(float(line[2]))
	
plt.errorbar(X,Y, yerr=Y_err)
plt.show() 
	
