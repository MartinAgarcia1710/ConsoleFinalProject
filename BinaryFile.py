import pickle as P

class File():
    def __init__(self, fileName):
        self.fileName = fileName

    def saveData(self, data):
            try:
                with open(self.fileName, "ab") as file:
                    P.dump(data, file)
                    file.close()
                    print("Saved successfully")
            except FileNotFoundError:
                print("FILE NOT FOUND")

    def loadData(self):
        try:
            with open(self.fileName, "rb") as file:
                data = P.load(file)
            print("Loaded successfully")
            file.close()
            return data
        except FileNotFoundError:
            print("FILE NOT FOUND")
            return