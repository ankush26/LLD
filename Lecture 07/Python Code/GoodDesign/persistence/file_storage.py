class FileStorage:
    def save(self, data):
        try:
            with open("document.txt", "w") as outFile:
                outFile.write(data)
                print("Document saved to document.txt")
        except IOError:
            print("Error: Unable to open file for writing.")