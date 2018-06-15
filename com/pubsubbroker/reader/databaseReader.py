### Licensed to SR ####
"""
Copyright SR(C)    2018
"""


from com.pubsubbroker.reader.genericreader import Reader
import sqlite3


class DatabaseReader(Reader):

    table_name = ''

    def __init__(self, name, table_name, mode='r'):
        self.object_name = sqlite3.connect(name)
        self.table_name = table_name

    def setter(self, name, table_name, mode='r'):
        self.object_name = sqlite3.connect(name)
        self.table_name = table_name

    def getter(self):
        return self.object_name

    def read_object(self):
        try:
            cursor = self.object_name.cursor()
            # The below line is just for testing
            cursor.execute('CREATE TABLE X (name CHAR, age int)')
            cursor.execute("insert into X values('ram',102)")
            cursor.execute("insert into X values('shyam',105)")
            self.resultSet = cursor.execute('select * from X')
            return self.resultSet
        except:
            cursor.close()
            self.destroy()


def main():
    f = DatabaseReader(":memory:", 'X')
    #print(f.getter())
    r = f.read_object()
    for i in r:
        print(i)
    f.destroy()


if __name__ == '__main__':
    main()
