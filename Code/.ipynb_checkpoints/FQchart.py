import matplotlib.pyplot as plt 
df = pd.read_csv('xydata.csv')
plt.figure(figsize=(10,8))
x, y = df['x'], df['y']
lable = df['coordination']
plt.scatter(x,y)
plt.xlabel('x'); plt.ylabel('y')