import math
import matplotlib.pyplot as plt
import numpy as np
pi = math.pi
g = 9.77

#initial conditions
W0 = 0.000  #Initial Angular Momentum
A0 = pi/4  #Initial Angle - measured from the pendulum normal, in Rads
length = 1+(np.sin(A0*W0))#1.00  #Length of the pendulum

tbegin = 1000 #Time start
tend = 1200   #Time end

h = 0.03 #step size
e = (tend-tbegin)/h  #modified loop range to correspond to time
C = -g/length #Pendulum constant

def Wfunc(Q):
    P = C*math.sin(Q)
    return P

#misc parameters
Wprev = W0
Aprev = A0
W =[]
A =[]
t =[]
'''W.append(W0)
A.append(A0)
t.append(tbegin)'''
#start of code

#transients adjustment
for n in range (0,int(tbegin/h)):
    k1 = Wfunc(Aprev)
    k2 = Wfunc(Aprev+((k1*h)/2))
    k3 = Wfunc(Aprev+((k2*h)/2))
    k4 = Wfunc(Aprev+((k3*h)))
    Wnow = Wprev+((h/6)*(k1+2*(k2+k3)+k4))
    l1 = Wnow
    l2 = Wnow+(l1*h/2)
    l3 = Wnow+(l2*h/2)
    l4 = Wnow+(l3*h)
    Anow = Aprev+((h/6)*(l1+2*(l2+l3)+l4))
    Wprev = Wnow
    Aprev = Anow

#main recording loop
for n in range (0,int(e)):
    k1 = Wfunc(Aprev)
    k2 = Wfunc(Aprev+((k1*h)/2))
    k3 = Wfunc(Aprev+((k2*h)/2))
    k4 = Wfunc(Aprev+((k3*h)))
    Wnow = Wprev+((h/6)*(k1+2*(k2+k3)+k4))
    l1 = Wnow
    l2 = Wnow+(l1*h/2)
    l3 = Wnow+(l2*h/2)
    l4 = Wnow+(l3*h)
    Anow = Aprev+((h/6)*(l1+2*(l2+l3)+l4))
    W.append(Wprev)
    A.append(Aprev)
    Wprev = Wnow
    Aprev = Anow
    #time counter
    tnow = tbegin+h
    t.append(tbegin)
    tbegin = tnow

#Degree conversion
Adeg=[]
for x in range (0,int(e)):
    Adeg.append(math.degrees(A[x]))
#print("Wnow is = ",W)
#print("Anow is =",Adeg)
#print("tnow is =",t)

#File Section
#to_write = "*Time values list*\n"+"time = {"+ str(t)[1:-1]+"}\n\n\n\n"+"*The Angular Momentum List*\n"+"momentum = {"+str(W)[1:-1]+"}\n\n\n\n"+"*The Phase value List*\n"+"angle = {"+str(Adeg)[1:-1]+"}\n\n\n"+"plotdata = Transpose[{time,angle}]\n"+"phaseplane = Transpose[{angle,momentum}]\n"+"ListPlot[plotdata]\n"+ "ListPlot[phaseplane]\n"
#to_write = "time = {"+ str(t)[1:-1]+"}\n"+"momentum = {"+str(W)[1:-1]+"}\n"+"angle = {"+str(Adeg)[1:-1]+"}\n"+"plotdata = Transpose[{time,angle}]\n"+"phaseplane = Transpose[{angle,momentum}]\n"+"ListPlot[plotdata]\n"+ "ListPlot[phaseplane]\n"
#Filehandling = open('E:/OutputFile.nb','w')
#Filehandling.write(to_write)
#Filehandling.close()

fig3 = plt.figure(figsize=(9,9),facecolor='white')
#fig3.suptitle('Rössler attractor Time Series\n Coupling Strength = %s'%(str(CS)),fontsize=18)
ax3 = fig3.add_subplot(1,1,1)
#ax3.plot(t, A, '-', color= 'tab:red',linewidth=0.5)
ax3.scatter(W,A,s=0.9)
ax3.set_ylabel('Angle', fontsize=15)
ax3.set_xlabel('Time',fontsize=15)
plt.tight_layout()
#fig3.savefig('E:\\myimage.svg', format='svg', dpi=12000)
plt.show()
