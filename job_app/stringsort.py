import sys
def stringsort(**kwargs):

    stringList = []
    for key, value in kwargs.iteritems():
        stringList.append(value)

    stringList.sort()
    print(stringList)
