from Users import session
import pandas as pd

file = pd.read_csv("user-song-rating.csv",sep=';')
df = pd.DataFrame(file,columns=['user','song','rating'])
def InputRating(Stars,SongId):
    for i, row in df.iterrows():
        if (row['user'] == session) and (row['song'] == SongId):
             df.at[i,'rating']=Stars
             df.to_csv('user-song-rating.csv',header=True,sep=";",index=False)
             break
        else:
             Rating= {'user':[session],
             'song':[SongId],
             'rating':[Stars]}
             Ratingdf=pd.DataFrame(Rating,columns=['user','song','rating'])
             newdf=df.append(Ratingdf,ignore_index=True)
             newdf.to_csv('user-song-rating.csv',header=True,sep=";",index=False)
   
   
InputRating(4,12)