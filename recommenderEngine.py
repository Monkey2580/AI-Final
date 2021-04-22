import pandas  # mostly just for DataFrames
from tabulate import tabulate  # tabulate DataFrames for easier viewing
import numpy
from scipy.spatial.distance import hamming  # hamming distance function
import pickle
import csv


class database:
    # NOTE: Unused!
    def __init__(self):
        self.users = ["user_alpha", "user_beta", "user_charlie", "user_delta", "user_epsilon", "user_foxtrot"]
        self.songs = []
        self.ratings = [  # y-axis = users, x-axis = songs. ratings 1-5, 0 denotes unrated
            [],
        ]

    def readCSV(self):
        with open("SONGS.csv", "r") as songlist:
            reader = csv.reader(songlist)
            index = 0  # index for songs tuple tracking
            for row in reader:
                if row[1] == "Title":  # exclude csv header
                    continue
                self.songs.append(row[1])  # append title of song
                index += 1
                if index == 5:  # take first 5 entries excluding "Title"
                    break

    def buildTable(self):
        self.ratings.pop()  # remove current entry in ratings
        numSongs = len(self.songs)
        for user in self.users:
            self.ratings.append([0] * numSongs)  # Create 0 list of song ratings for each user

    def testMode(self):
        """
        Builds an example dataset for a 6 user 5 song table.
        Do not use for actual deployment.

        :return:
        """
        print("Test Mode: Building and using test dataset")
        self.readCSV()
        self.buildTable()

        """
        Example dataset:
        X   s1  s2  s3  s4  s5
        u1  3   4   0   0   4
        u2  3   5   3   4   5
        u3  4   2   0   5   4
        u4  3   0   4   5   2
        u5  1   0   4   2   1
        u6  3   4   0   2   5
        Damn this is repetitive
        """
        self.ratings[0] = [3, 4, 0, 0, 4]
        self.ratings[1] = [3, 5, 3, 4, 5]
        self.ratings[2] = [4, 2, 0, 5, 4]
        self.ratings[3] = [3, 0, 4, 5, 2]
        self.ratings[4] = [1, 0, 4, 2, 1]
        self.ratings[5] = [3, 4, 0, 2, 5]
        #for user in self.ratings:
        #    for songRating in user:
        #        pass


class engine:
    """
    Recommender engine implementation using collaborative filtering
    """

    def __init__(self):
        self.songList = None
        self.userRatings = None
        self.ratingMatrix = None


    def engineTestMode(self):
        self.songList = pandas.read_csv("songs-test.csv", sep=",", header=0, index_col=0, names=["SongID", "Title", "ArtistName", "AlbumName", "Duration"])
        self.userRatings = pandas.read_csv("user-song-rating.csv", sep=";", header=0, names=["UserID", "SongID", "Rating"])
        print(tabulate(self.songList.head(5), headers="keys", tablefmt='psql'))  # sanity check, display first 5 entries
        print(tabulate(self.userRatings.head(5), headers="keys", tablefmt='psql'))  # sanity check, display first 5 entries
        self.userRatings = self.userRatings[self.userRatings["SongID"].isin(self.songList.index)]  # Check that every Song ID referenced in self.ratings exists in self.songList
        #print(self.getSongByID(2))
        print("\n")
        #print(self.userFavoriteSongs("u1", 2))

        usersPerSongID = self.userRatings.SongID.value_counts()  # includes empty entries
        print("Unique songs:", usersPerSongID.shape[0])  # number of song entries
        print(usersPerSongID)  # number of users who have rated a song
        print("\n")
        SongIDPerUser = self.userRatings.UserID.value_counts()
        print("Unique users:", SongIDPerUser.shape[0])  # number of users
        print(SongIDPerUser)  # number of songs that a user has rated
        print("\n")
        self.buildRatingMatrix()
        print(self.ratingMatrix, "\n")
        self.checkUserSimilarity("u1", "u2")

    def buildRatingMatrix(self):
        """
        Initialize rating matrix.
        User populates y-axis.
        Songs populates x-axis.
        Each cell represents a rating corrosponding to a user(y) for a given song(x)
        Make sure self.ratings is properly loaded and initialized beforehand.
        :return:
        """
        userAxis = self.userRatings.UserID.value_counts()
        songAxis = self.userRatings.SongID.value_counts()
        # self.userRatings = self.userRatings[self.userRatings["SongID"].isin(userAxis[userAxis>10].index)]  # Restrict data to only include users who have rated n-number of songs (replace n)
        # self.userRatings = self.userRatings[self.userRatings["UserID"].isin(userAxis[songAxis>10].index)]  # Restrict data to only include songs that has been rated n-number of times (replace n)
        self.ratingMatrix = pandas.pivot_table(self.userRatings, values="Rating", index=["UserID"], columns=["SongID"])
        print("Rating Matrix generated:", songAxis.shape[0], "columns,", userAxis.shape[0], "rows")

    def getSongByID(self, song_id):
        title = self.songList.at[song_id, "Title"]
        artist = self.songList.at[song_id, "ArtistName"]
        album = self.songList.at[song_id, "AlbumName"]
        return title, artist, album

    def userFavoriteSongs(self, user, n):
        """
        Get the specified user's top n rated songs
        :param user: user's id
        :param n: number of songs to retrieve
        :return:
        """
        userRatings = self.userRatings[self.userRatings["UserID"] == user]
        sortedRatings = pandas.DataFrame.sort_values(userRatings, ["Rating"], ascending=[0])[:n]
        sortedRatings["Title"] = sortedRatings["SongID"].apply(self.getSongByID)
        return sortedRatings

    def predictRatings(self, user):
        """
        Takes in user's song ratings and predicts ratings of 0-entries using nearest neighbours.
        :param user: List of a user ratings
        :return: List of predicted ratings of unrated songs
        """
        pass

    def checkUserSimilarity(self, user1, user2):
        """
        Checks a user's similarities against another user using hamming distance.
        Returns an integer value that represents similarity.
        0 -> No differences in rating, highly similar.
        Higher values denote dissimilarity.
        :param user1: User 1's ratings
        :param user2: User 2's ratings
        :return: Integer, similarity value
        """
        user1Ratings = self.ratingMatrix.transpose()[user1]  # get user's ratings for all songs (includes unrated as NaN)
        print(user1Ratings)
        user2Ratings = self.ratingMatrix.transpose()[user2]
        print(user2Ratings)
        distance = hamming(user1Ratings, user2Ratings)
        print(distance)


if __name__ == "__main__":
    """
    This module is to be imported to a client file/module. 
    It is not designed to be run directly.
    """
    engine = engine()
    engine.engineTestMode()
