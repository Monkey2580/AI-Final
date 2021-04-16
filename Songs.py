import csv
from SongDetails import SongsDetails
Songs_array = []

with open("SONGS.csv",'r',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        DurationInSecs = float(row["Duration"])/ 60 
        Songs_array.append(SongsDetails(row["Title"],row["ArtistName"],row["AlbumName"],DurationInSecs))