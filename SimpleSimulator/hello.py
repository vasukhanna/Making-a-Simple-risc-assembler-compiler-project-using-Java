import random as r
import numpy as np
import matplotlib.pyplot as plt

lx = []
ly = []


def read_data_from_file(file_path="output.txt"):
    with open(file_path,'r') as data:
        l=[]
        records=data.read()
        records=records.replace("/n"," ")
        l=records.splitlines()
        for i in l:
            lx.append(int(i.split(" ")[0]))
            ly.append(int(i.split(" ")[1]))



def plot(x_d, y_d):
    x_d, y_d = 1.2 * x_d, 1.2 * y_d
    plt.plot((0,x_d),[0,0], 'k-')
    plt.plot([0,0],(0,y_d), 'k-')

    plt.xlim(0,x_d)
    plt.ylim(0,y_d)

    plt.grid()
    x=r.randint(0,10000)
    plt.savefig("Ques3"+str(x)+".png")
    plt.show()


def pello(x, y):
    plt.scatter(x, y)
    plot(max(x), max(y))

read_data_from_file()

pello(lx,ly)
