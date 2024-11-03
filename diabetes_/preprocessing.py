import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\vscode\diabetes\diabetes.csv')

x = df.drop("Outcome", axis=1)
y = df["Outcome"]

df["Outcome"].value_counts()
x = np.array(x)
y= np.array(y)