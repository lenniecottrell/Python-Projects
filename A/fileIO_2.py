import os
from datetime import datetime, timezone

##fileName = "text2.txt"
##filePath = "C:\\Users\\lenni\\Documents\\GitHub\\Python-Projects\\A\\"
##absPath1 = os.path.join(filePath, fileName)


for file in os.listdir(path='C:\\Users\\lenni\\Documents\\GitHub\\Python-Projects\\A\\'):
    filePath = os.path.join('C:\\Users\\lenni\\Documents\\GitHub\\Python-Projects\\A\\', file)
    pathMod = os.path.getmtime(filePath)
    easyPath = datetime.fromtimestamp(pathMod)
    if file.endswith(".txt"):
        print(os.path.join('C:\\Users\\lenni\\Documents\\GitHub\\Python-Projects\\A\\', file) + "\n\tLast modified: " + str(easyPath))

