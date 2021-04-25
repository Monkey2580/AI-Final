from SongDetails import SongsDetails #Class
from Songs import Songs_array #Songs array with class 
from RatingSystem import InputRating
from Users import session
counter = 0
#for calling the songs description
for x in Songs_array:
    if counter <5:
        print(x.Title)
        print(x.Artist)
        print(x.Album)
        print(x.Duration)
    counter+=1

#input song rating
User = session
Songrating = 4
SongsId=102
InputRating(User,Songrating,SongsId)