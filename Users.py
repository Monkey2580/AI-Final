import pandas as pd


user = input("User using: ")
Userlower=user.lower()
df = pd.read_csv("Userlist.csv",sep=';')
for i in df.iloc[:,0].str.lower():
    if Userlower == i:
        session = user
        break
    