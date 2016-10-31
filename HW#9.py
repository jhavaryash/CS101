import numpy as np 
#Parameters of simulation
n=5000 			#number of data points
start=0.0 		# start time, s
end=4500.0 		#end time, s
a=-8.87			#acceleration, m/s^2

#State variable initialization
t=np.linspace(start,end,n+1) #time, s
y=np.zeros(n+1) 			 #height, m
v=np.zeros(n+1) 			 #velocity, m/s^2
y[0] = 250000.0				 #height, m
bounces=0

#looping to drop the ball
for i in range(1,n+1):
	v[i]=v[i-1] + a*(t[i]-t[i-1]) 		# v=u+at
	y[i]=y[i-1]+v[i-1]*(t[i]-t[i-1]) 	#add distance travelled in timestep
	
	if y[i] <= 0: 			#if ball has hit the ground
		bounces+=1			#increment bounces counter
		y[i]=0				#change height to ZERO
		v[i]=-0.9*v[i-1]    #Change direction of speed & and apply bounce factor 0.9

#plotting the given data. x=time and y=height
import matplotlib.pyplot as plt    	#Import library for plot() 
plt.plot(t,y,'m:')   				#plot, m: = magenta dots
plt.ylabel('Height (m)')            #label y axis
plt.xlabel('Time (s)')              #label y axis
plt.title('Bouncing on Venus')      #label title
#plt.show() 