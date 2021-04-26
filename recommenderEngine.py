import pandas  # mostly just for DataFrames
from tabulate import tabulate  # tabulate DataFrames for easier viewing
import numpy
from scipy.spatial.distance import hamming  # hamming distance function


class engine:
    """
    Recommender engine implementation using collaborative filtering
    """

    def __init__(self):
        self.songList = None
        self.userRatings = None
        self.ratingMatrix = None

    def engineTestMode(self):
        """
        For testing only
        :return:
        """
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

        #self.checkUserSimilarity("u1", "u2")
        recommendations = self.generateRecommendations("u1", 3)
        print(recommendations)

    def loadData(self, printData=False):
        """
        Load data from csv files to songList and userRatings.
        Call this before doing anything.
        """
        self.songList = pandas.read_csv("songs-test.csv", sep=",", header=0, index_col=0,
                                        names=["SongID", "Title", "ArtistName", "AlbumName", "Duration"])
        self.userRatings = pandas.read_csv("user-song-rating.csv", sep=";", header=0,
                                           names=["UserID", "SongID", "Rating"])
        if printData:
            print(tabulate(self.songList))
            print(tabulate(self.userRatings))

    def getUserRating(self, user, song):
        """
        Returns the specified user's ratings for the specified song.
        Returns None if user has not rated the specified song.
        :param user:
        :param song:
        :return:
        """
        rowIndex = 0
        entryFound = False
        userRatingEntry = self.userRatings.drop("Rating", 1)  # copy userRating dataframe without rating column
        userRatingEntry = userRatingEntry.isin([user, song])
        userRatingEntry = userRatingEntry.to_numpy()
        for row in userRatingEntry:
            #print(row[0])
            #print(row[1], "\n")
            if row[0] and row[1]:  # if a user has already rated the specified song
                return self.userRatings.loc[rowIndex]
            else:
                rowIndex += 1

        return None

    def updateUserRating(self, user, song, rating, updateMatrix=True):
        """
        Updates or adds a user's rating of a song to userRatings based on supplied parameters.
        Remember to call buildRatingMatrix() afterwards to update ratingMatrix.
        :return:
        """
        rowIndex = 0
        entryFound = False
        userRatingEntry = self.userRatings.drop("Rating", 1)  # copy userRating dataframe without rating column
        userRatingEntry = userRatingEntry.isin([user, song])
        userRatingEntry = userRatingEntry.to_numpy()
        #print(userRatingEntry, "\n")

        for row in userRatingEntry:  # iterate over rows
            #print(row[0])
            #print(row[1], "\n")
            if row[0] and row[1]:  # if a user has already rated the specified song
                self.userRatings.loc[rowIndex] = [user] + list([song, rating])  # update a user's rating for the song
                entryFound = True
                break
            else:
                rowIndex += 1

        if not entryFound:  # user has not previously rated the specified song
            newMaxIndex = self.userRatings.index.max() + 1
            self.userRatings.loc[newMaxIndex] = [user] + list([song, rating])

        if updateMatrix:
            self.buildRatingMatrix()

    def buildRatingMatrix(self):
        """
        Initialize or update rating matrix.
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
        print("Rating Matrix generated:", songAxis.shape[0], "columns (songs),", userAxis.shape[0], "rows (users)")

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

    def generateRecommendations(self, user, n):
        """
        Generates n-number of recommendations for the specified user
        Returns a tuple containing songs and its data, recommendation in descending order.
        Number of recommendations may be lower than n specified.

        :param user: String, user id
        :param n: Int, (max) number of recommendations
        :return: Tuple[List()]
        """
        recommendationTuple = []

        nearestUsers = self.nearestNeighbours(user, n)
        neighbourRatings = self.ratingMatrix[self.ratingMatrix.index.isin(nearestUsers)]
        avgRating = neighbourRatings.apply(numpy.nanmean).dropna()
        listenedSongs = self.ratingMatrix.transpose()[user].dropna().index
        avgRating = avgRating[~avgRating.index.isin(listenedSongs)]
        recommendations = avgRating.sort_values(ascending=False).index[:n]
        reccomendationList = pandas.Series(recommendations).apply(self.getSongByID)

        # Reformat to basic tuple
        for recommendation in reccomendationList:
            recommendationTuple.append(recommendation)

        return recommendationTuple  # Returns recommendation in desending order

    def nearestNeighbours(self, user, n):
        """
        Get n-number of nearest neighbours of specified user.
        Distance calculated using self.checkUserSimilarity()
        :param user: UserID
        :param n: Int, number of neighbours to return
        :return: DataFrame, n-number of neighest neighbour and their ratings
        """
        allUsers = pandas.DataFrame(self.ratingMatrix.index)  # copy matrix
        allUsers = allUsers[allUsers.UserID != user]  # remove active user from current dataset
        allUsers["Distance"] = allUsers["UserID"].apply(lambda x: self.checkUserSimilarity(user, x))
        nearestUsers = allUsers.sort_values(["Distance"], ascending=True)["UserID"][:n]  # structure: Index, UserID
        return nearestUsers

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
        #print(user1Ratings)
        user2Ratings = self.ratingMatrix.transpose()[user2]
        #print(user2Ratings)
        try:
            distance = hamming(user1Ratings, user2Ratings)
            #print(distance)
        except:
            distance = numpy.NaN
        return distance


if __name__ == "__main__":
    """
    This module is to be imported to a client file/module. 
    It is not designed to be run directly.
    Below is an example of an implementation.
    """
    engine = engine()
    #engine.engineTestMode()
    engine.loadData()
    engine.buildRatingMatrix()
    print(engine.ratingMatrix, "\n")
    #print(engine.userRatings, "\n")

    recommendations = engine.generateRecommendations("u1", 3)
    print(recommendations, "\n")

    userRatingTest = engine.getUserRating("u6", 125)
    if userRatingTest is None:
        print("User has not rated that song yet")
    else:
        print(userRatingTest.Rating)


    """
    engine.updateUserRating("u5", 114, 4)
    print(engine.userRatings, "\n")

    engine.updateUserRating("u1", 101, 5)
    print(engine.userRatings, "\n")
    """
