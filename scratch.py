import  pickle

class scratch:

    class data:

        def __init__(self):
            self.users = ["user_alpha", "user_beta", "user_charlie", "user_delta", "user_epsilon"]
            self.songs = ["song_alpha", "song_beta", "song_charlie"]
            self.testStr = "Hello World!"
            self.testInt = 10
            self.testFloat = 3.14

        def __str__(self):
            return f'users: {self.users}\n' \
                   f'songs: {self.songs}\n' \
                   f'testStr: {self.testStr}\n' \
                   f'testInt: {self.testInt}\n' \
                   f'testFloat: {self.testFloat}\n'

    def exportData(self):
        print("Exporting:")
        dataFile = open("test.pkl", "ab")  # file name (relative directory), open in [a]ppend mode handled as [b]inary
        dataInstance = scratch.data()  # put class into variable
        print(dataInstance)
        pickle.dump(dataInstance, dataFile, -1)  # export
        dataFile.close()  # remember to close any files from open()

    def importData(self):
        with open("test.pkl", "rb") as dataFile:  # file name (relative directory), open in read mode handled as [b]inary
            data = pickle.load(dataFile)
            print(data)  # __str__ does not work
            print(data.users)
        dataFile.close()


if __name__ == "__main__":
    """
    For testing blocks of code and dicking around in general
    """
    scratch = scratch()
    #scratch.exportData()
    scratch.importData()
