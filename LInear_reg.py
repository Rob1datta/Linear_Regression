import numpy as np
import matplotlib.pyplot as plt
import re

class Linear1D:
    def __init__(self):
        print "ok now constructing your class"
    def __del__(self):
        print "ok now  destructing your class"
    def Linear1D_data(self):
        #Empty lists to create datasets
        X=[]
        Y=[]
        # Reading the csv data
        for line in open("/home/myboxuser/Downloads/Data/data_1d.csv"):
            x,y=line.split(',')
            #print x,y
            X.append(float(x))
            Y.append(float(y))
        Xarray=np.array(X)
        Yarray=np.array(Y)
        plt.scatter(Xarray,Yarray)
        denominator =(Xarray.dot(Xarray))- (Xarray.mean() * Xarray.sum())
        aslope = (Xarray.dot(Yarray) - Yarray.mean() * Xarray.sum()) / denominator
        b = (Yarray.mean() * Xarray.dot(Xarray) - Xarray.mean() * Xarray.dot(Y)) / denominator

        Yhat=aslope*Xarray+b
        plt.scatter(Xarray,Yhat)
        plt.show()
        #Calculate the Rsquared
        d1=Yarray-Yhat
        d2=Yarray-Yarray.mean()
        r2_squared=1-d1.dot(d1)/d2.dot(d2)
        print r2_squared

    def Moorelaw(self):
        X=[]
        Y=[]
        non_decimal=re.compile(r'[^\d]+')
        for line in open('/home/myboxuser/Downloads/Data/moore.csv'):
            r=line.split('\t')
            x = int(non_decimal.sub('', r[2].split('[')[0]))
            y = int(non_decimal.sub('', r[1].split('[')[0]))
            X.append(x)
            Y.append(y)
        Xarray=np.array(X)
        Yarray=np.array(Y)
        plt.scatter(Xarray,Yarray)
        plt.show()
        Yarray=np.log(Yarray)
        denominator = (Xarray.dot(Xarray)) - Xarray.mean() * Xarray.sum()
        aslope = (Xarray.dot(Yarray) - Yarray.mean() * Xarray.sum()) / denominator
        b = (Yarray.mean() * Xarray.dot(Xarray) - Xarray.mean() * Xarray.dot(Yarray)) / denominator

        Yhat = aslope * Xarray + b
        plt.plot(Xarray, Yhat)
        plt.show()

        d1=Yarray-Yhat
        d2=Yarray-Yarray.mean()
        r2 = 1 - d1.dot(d1) / d2.dot(d2)
        print aslope,b,r2

        time_to_double=np.log(2.03)/aslope
        print "The predicted year to double is ",time_to_double
















make=Linear1D()
make.Moorelaw()

