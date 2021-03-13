import os.path

testcsv=open("test.csv", "r")
lines=testcsv.readlines()
count=0
for line in lines:
    parts=line.split()
    filePathToAppend=os.path.join("data", parts[0].replace(".jpg",".txt"))
    labelFileHandle=open(filePathToAppend, 'a')
    x=int(parts[1])
    y=int(parts[2])
    w=int(parts[3])
    h=int(parts[4])

    topLeftX=x
    topLeftY=y
    topRightX=x+w
    topRightY=y
    bottomLeftX=x
    bottomLeftY=y+h
    bottomRightX=x+w
    bottomRightY=y+h
    labelFileHandle.write("{}, {}, {}, {}, {}, {}, {}, {}, ###\n".format(topLeftX, topLeftY, topRightX, topRightY, bottomLeftX, bottomRightY, bottomLeftY, bottomRightX))
    labelFileHandle.close()
testcsv.close()