from re import A
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("x5.04.2022\kopia.csv")
a = []
a = df['id'].to_list()
b = []
b = df['srednia'].to_list()

plt.bar(a,b)
plt.show()
