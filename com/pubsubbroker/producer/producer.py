### Licensed to SR ####
"""
Copyright SR(C)    2018
"""

from com.pubsubbroker.reader.filereader import FileReader
from time import sleep

f = FileReader('D:\Tasks.txt')

try:
    while 1==1:
        r = f.read_object()
        print(r)
        sleep(5)
finally:
    f.destroy()

