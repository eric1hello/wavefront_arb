#!/usr/bin/python3
import sys
import numpy as np

def cell( x,y,pri,req):
    xpri = x & pri
    ypri = y & pri
    grant = req & ypri & xpri

    grant_n = ~grant
    yout = ypri & grant_n
    xout = xpri & grant_n
    
    return xout,yout,grant

def wavefront_arb(x_token,y_token,pri,req):
    # x=row, y=colum
    grant=np.array([[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]])
    x_token[0][1],y_token[1][0],grant[0][0] = cell(x_token[0][3],y_token[3][0],pri[0],req[0][0])
    x_token[3][2],y_token[0][1],grant[3][1] = cell(x_token[3][0],y_token[2][1],pri[0],req[3][1])
    x_token[2][3],y_token[3][2],grant[2][2] = cell(x_token[2][1],y_token[1][2],pri[0],req[2][2])
    x_token[1][0],y_token[2][3],grant[1][3] = cell(x_token[1][2],y_token[0][3],pri[0],req[1][3])
    pri = np.roll(pri,1)
    
    if (grant[0][0]) :
        x_token[0,:] = 0
        y_token[:,0] = 0

    if (grant[3][1]) :
        x_token[3,:] = 0
        y_token[:,1] = 0

    if (grant[2][2]) :
        x_token[2,:] = 0
        y_token[:,1] = 0

    if (grant[1][3]) :
        x_token[1,:] = 0
        y_token[:,3] = 0

   # print(x_token)
   # print(y_token)
   # print(grant)
   # print("wave 0 \n")


    x_token[1][1],y_token[2][0],grant[1][0] = cell(x_token[1][3],y_token[0][0],pri[1],req[1][0])
    x_token[0][2],y_token[1][1],grant[0][1] = cell(x_token[0][0],y_token[3][1],pri[1],req[0][1])
    x_token[3][3],y_token[0][2],grant[3][2] = cell(x_token[3][1],y_token[2][2],pri[1],req[3][2])
    x_token[2][0],y_token[3][3],grant[2][3] = cell(x_token[2][2],y_token[1][3],pri[1],req[2][3])
    pri = np.roll(pri,1)

    if (grant[1][0]) :
        x_token[1,:] = 0
        y_token[:,0] = 0

    if (grant[0][1]) :
        x_token[0,:] = 0
        y_token[:,1] = 0

    if (grant[3][2]) :
        x_token[3,:] = 0
        y_token[:,2] = 0

    if (grant[2][3]) :
        x_token[2,:] = 0
        y_token[:,3] = 0

   # print(x_token)
   # print(y_token)
   # print(grant)
   # print("wave 1 \n")

    x_token[2][1],y_token[3][0],grant[2][0] = cell(x_token[2][3],y_token[1][0],pri[2],req[2][0])
    x_token[1][2],y_token[2][1],grant[1][1] = cell(x_token[1][0],y_token[0][1],pri[2],req[1][1])
    x_token[0][3],y_token[1][2],grant[0][2] = cell(x_token[0][1],y_token[3][2],pri[2],req[0][2])
    x_token[3][0],y_token[0][3],grant[3][3] = cell(x_token[3][2],y_token[2][3],pri[2],req[3][3])
    pri = np.roll(pri,1)

    if (grant[2][0]) :
        x_token[2,:] = 0
        y_token[:,0] = 0

    if (grant[1][1]) :
        x_token[1,:] = 0
        y_token[:,1] = 0

    if (grant[0][2]) :
        x_token[0,:] = 0
        y_token[:,2] = 0

    if (grant[3][3]) :
        x_token[3,:] = 0
        y_token[:,3] = 0

   # print(x_token)
   # print(y_token)
   # print(grant)
   # print("wave 2 \n")

    x_token[3][1],y_token[0][0],grant[3][0] = cell(x_token[3][3],y_token[2][0],pri[3],req[3][0])
    x_token[2][2],y_token[3][1],grant[2][1] = cell(x_token[2][0],y_token[1][1],pri[3],req[2][1])
    x_token[1][3],y_token[2][2],grant[1][2] = cell(x_token[1][1],y_token[0][2],pri[3],req[1][2])
    x_token[0][0],y_token[1][3],grant[0][3] = cell(x_token[0][2],y_token[3][3],pri[3],req[0][3])
    pri = np.roll(pri,1)

    #print(x_token)
    #print(y_token)
    #print(grant)
    #print("end \n")

    return x_token,y_token,pri,grant

if __name__ == '__main__':
    
       
    req=np.array([[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]])

    pri=np.array([1,0,0,0])
    for j in range(1):
        x_token=np.array([[1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1]])
        y_token=np.array([[1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1]])
        x_token,y_token,pri,grant = wavefront_arb(x_token,y_token,pri,req)
        print(grant)

