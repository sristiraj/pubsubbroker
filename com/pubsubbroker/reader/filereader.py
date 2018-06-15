### Licensed to SR ####
"""
Copyright SR(C)    2018
"""


from com.pubsubbroker.reader.genericreader import Reader


class FileReader(Reader):

    def __init__(self, name, mode='r'):
        try:
            self.object_name = open(name, mode)
        except:
            print("Error reading file! Please check if the file exist!")
            raise

    def setter(self, name, mode='r'):
        try:
            self.object_name = open(name, mode)
        except:
            print("Error reading file")
            raise

    def getter(self):
        return self.object_name

    def read_object(self):
        try:
            self.resultSet = self.object_name.read()
            return self.resultSet
        except:
            print("No such object exist")
            self.destroy()
            raise


def main():
    f = FileReader('C:\windows-version.txt', 'r')
    #print(f.getter())
    r = f.read_object()
    print(r)
    f.destroy()


if __name__ == '__main__':
    main()
