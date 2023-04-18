import numpy as np

file1=open('/Users/devanshsingh/Desktop/data1lenghts.txt','r')
lengths=file1.readlines()
file2=open('data2angles.txt','r')
theta=file2.readlines()
a1=float(lengths[0])
a2=float(lengths[1])
a3=float(lengths[2])
T1D=float(theta[0])
T2D=float(theta[1])
#Changing degrees to radians
T1=(T1D/180)*np.pi
T2=(T2D/180)*np.pi
d3=4
r01=[[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]
r12=[[-np.sin(T2),0,np.cos(T2)],[np.cos(T2),0,np.sin(T2)],[0,1,0]]
r23=[[1,0,0],[0,1,0],[0,0,1]]

r02=np.dot(r01,r12)
r03=np.dot(r02,r23) #resultant Rotational Matrix

d01=[[0],[0],[a1]]
d12=[[0],[0],[0]]
d23=[[0],[0],[a2+a3+d3]]
#Homogeneous Transformation matrix
h01=np.concatenate((r01,d01),1)
h01=np.concatenate((h01,[[0,0,0,1]]),0)
h12=np.concatenate((r12,d12),1)
h12=np.concatenate((h12,[[0,0,0,1]]),0)
h23=np.concatenate((r23,d23),1)
h23=np.concatenate((h23,[[0,0,0,1]]),0)

h02=np.dot(h01,h12)
h03=np.dot(h02,h23)
print(h03)



