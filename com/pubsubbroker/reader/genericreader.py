### Licensed to SR ####
"""
Copyright SR(C)    2018
"""


class Reader:

    object_name = object()
    mode = 'r'
    resultSet = ''

    def __init__(self, name, mode = 'r'):
        pass

    def getter(self):
        return self.object_name

    def setter(self, name, mode='r'):
        pass

    def read_object(self):
        pass
    def write_object(self):
        pass

    def destroy(self):
        print("Destroying Reader object")
        self.object_name.close()

