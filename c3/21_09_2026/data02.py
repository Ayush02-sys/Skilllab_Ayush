import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#1st way

# g=np.random.default_rng(42)
# d=g.integers(25,51,size=(5,6))
# dg=["user1","user2","user3","user4","user5"]
# health_rec=["sugar","bp","BMI","spo2","risk score","heart_rate"]
# print(plt.figure(figsize=(10,6)))
# df=pd.DataFrame(data=d, index=dg, columns=health_rec)
# print(df)
# print("-"*50)
# print()

#or

#2nd way

#generating sample
np.random.seed(42)
df=pd.DataFrame({
    "Sleeping_Hours":np.random.randint(1,15,24),
    "Walk_hours":np.random.randint(20,40,24),
    "workout_hours":np.random.randint(5,30,24),
    "Assesment":np.random.randint(2,15,24)
})

df["Performance"]=np.where(df["workout_hours"]>=20,"High","Low")
print(df)

sns.scatterplot(
    data=df, x="Sleeping_Hours",y="workout_hours", hue="Performance"
)
plt.title("Performance of Workout based on sleeping hours")
print(plt.show())