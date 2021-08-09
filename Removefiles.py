import os
import shutil
import time

path = input("Path to removable files: ")
days = input("Delete files from before: ")
timeComparer = (time.time())-1*86400

for fileName in os.listdir(path):
    if os.path.getatime(os.path.join(path,fileName))<timeComparer:
        if os.path.isfile(os.path.join(path,fileName)):
            print(fileName)
            os.remove(os.path.join(path,fileName))

        elif os.path.isdir(os.path.join(path,fileName)):
            print(fileName)
            shutil.rmtree(os.path.join(path,fileName))