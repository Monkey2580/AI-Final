import pandas
import pickle
import csv


class database:

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
        self.db = database()

    def engineTestMode(self):
        self.db.testMode()
        print("User List:", self.db.users)
        print("Song List:", self.db.songs)
        print("Ratings Table: ")
        print(self.db.ratings)

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
        pass


if __name__ == "__main__":
    """
    This module is to be imported to a client file/module. 
    It is not designed to be run directly.
    """
    engine = engine()
    engine.engineTestMode()
