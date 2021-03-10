#ライブラリの設定
import pandas as pd
import matplotlib.pyplot as plt

def plot(xlabel,ylabel,x,y,file_name):
    #データロード
    df = pd.read_excel(file_name)
    #フォント
    plt.rcParams['font.family'] = 'Times New Roman' #フォント一括
    plt.rcParams["font.size"] = 20
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.direction'] = 'in'
    plt.scatter(df.iloc[:,x],df.iloc[:,y],c="white",linewidths="1",edgecolors="red")
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xlim(0)
    plt.ylim(0)
    plt.savefig(file_name+".png")
    
plot("Input current (A)","Output power (mW)",0,1,"mopafinfin.xlsx")
