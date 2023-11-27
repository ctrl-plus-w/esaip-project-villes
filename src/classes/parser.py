class Parser:
    def __init__(self, data: str):
        self.data = data

    @staticmethod
    def retrieve_data(path: str):
        """Return the data from the file content from the path"""
        file = open(path)

        for line in file.read().split("\n"):
            print(line)

    def parse(self):
        """Parse the data from the data property of the class"""
        data = self.data
        # for ligne in data:

        # return
