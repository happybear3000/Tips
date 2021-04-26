import matplotlib.pyplot as plt 
import pandas as pd

path = "xydata.csv"
df = pd.read_csv(path,encoding='gbk')
plt.figure(figsize=(10,8))
x, y = df['x'], df['y']
label = df['coordination']
plt.scatter(x,y)
plt.xlabel('x'); plt.ylabel('y')