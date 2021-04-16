from SongDetails import SongsDetails #Class
from Songs import Songs_array #Songs array with class 

counter = 0
#print list of songs
for x in Songs_array:
    if counter <5:
        print(x.Title)
        print(x.Artist)
        print(x.Album)
        print(x.Duration)
    counter+=1
