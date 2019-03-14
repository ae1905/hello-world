# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:54:14 2018

check data one by one 

@author: LX
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

data1 = np.load('data1_7_3.npy').item()
data2 = np.load('data2_7_3.npy').item()
data3 = np.load('data3_7_3.npy').item()

X=np.concatenate((data1['raw_X'],data2['raw_X'],data3['raw_X']), axis=0)
y=np.concatenate((data1['y'],data2['y'],data3['y']), axis=0)
N=y.shape[0]

print(N)
"""show singal"""
index=np.arange(y.shape[1])

def show_one_dif(i=0):

    plt.figure(figsize=(16, 8))
    fig, axs = plt.subplots(2,1,sharex=False)
    axs[0].plot(X[i])
    axs[1].plot(index, y[i],'--', color="k")
    
    plt.show()
    fig.savefig("signal_%d.png" % i)

    plt.close()    
    
show_one_dif(0)
#
#def show_imgs(X,y,index=0,r=10):
#    
#    r= r
#    
#    plt.figure(figsize=(10, 10))
#    fig, axs = plt.subplots(r,1,sharex=True)
#    cnt = index
#    for i in range(r):
#        axs[i].plot(X[cnt])
#        axs[i].axvline(x=y[cnt][0],color='green')
#        axs[i].axvline(x=y[cnt][1],color='red')
#        cnt += 1
#        axs[i].axes.get_yaxis().set_visible(False)
#    fig.savefig("signal_%d.png" % index)
##    plt.show()
#    plt.close()
#
    

    

#for i in range(int(N/10)):
#    index=i*10
#    show_imgs(X,y,index=index,r=10)
#    
#show_imgs(X,y,index=N-N%10,r=N%10)
#    

"""show stft"""

#fs=25600
#
#nperseg=1024
#df=fs/nperseg
#print('频率分辨率',df)
#f_start=200
#f_end=2150
#f_l=int(f_start/df)
#f_u=int(f_end/df+1)

#x=p0[45]

#def stft(x):
#    _, _, Zxx = signal.stft(x, fs, nperseg=nperseg)
#    temp=np.abs(Zxx[f_l:f_u,1:])
#    return temp/np.max(temp)
#
#  
#f, t, Zxx = signal.stft(X[1], fs, nperseg=nperseg)
#
##plt.pcolormesh(t, f, np.abs(apply_to_magnitude(Zxx)))
##f=f[f_l:f_u]
##t=t[1:]
##Zxx=Zxx[f_l:f_u,1:]
#vmax=np.max(abs(Zxx))
#plt.pcolormesh(t, f, np.abs(Zxx),vmin=0, vmax=vmax)
#plt.title('STFT Magnitude')
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()
#
#dele_list=[12,23,34,47,50,64,84,89,94,98,100,102,114,118,130,132,138,
#           140,160,171,174,176,189,199,202,210,216,219,220,229,244,
#           245,255,279,284,297,320,323,335,336,348,349,359,365,373,
#           386,392,393,394,395,408,410,439,442,443,466,470,472,473,
#           483,498,505,506,508,509,513,515,517,519,523,526,527,534,
#           544,545,552,554,555,556,559,560,564,567,568,577,580,582,
#           588,591,595,601,604,609,610,613,614,615,619,620,623,624,
#           628,629,631,634,638,642,644,645,647,652,660,664,670,671,
#           677,680,681,683,685,687,690,691,692,693,696,709,710,715,
#           716,718,724,730,734,738,740,746,750,757,761,762,768,775,
#           776,789,791,793,795,798,801,802,803,806,807,808,809,810,
#           811,812,813,816,817,818,819,820,822,824,826,828,832,837,
#           839,840,842,843,848,849,852,854,855,857,859,861]
#dele_a=np.array(dele_list)
#
#print(N)
#print(dele_a.shape)
#
#X2=np.delete(X,dele_a,axis=0)
#y2=np.delete(y,dele_a,axis=0)
#
#print(X2.shape)
#print(y2.shape)
#
#data2={}
#
#data2['X']=X2
#data2['y']=y2
#np.save('mingdi_data628_pre.npy', data2) 