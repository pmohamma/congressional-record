import os


def main():
    rootdir = 'C:/Users/pouya\python-projects\congressional-record\congressionalrecord\output'
    writer = open("writer.txt", 'w')
    writer.close()
    dirtyWriter = open("dirtyWriter.txt", 'w')
    dirtyWriter.close()

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.htm'):
                fname = subdir + '\\' + file
                f = open(fname, 'r')
                contents = ""
                for line in f:
                    contents += line
                    # print (os.path.join(subdir, file))
                f.close()
                contents = cleanContents(contents)
                dirtyWriter = open("dirtyWriter.txt", 'a')
                dirtyWriter.write(contents)
                dirtyWriter.close()
                contents = cleanForSpeeches(contents)
                #print(contents)


def cleanContents(contents):
    bodystart = contents.index('<body>') + 6
    bodyend = contents.index('</body>')
    ret = contents[bodystart:bodyend]
    if (ret.index("<pre>") != -1):
        retstart = ret.index('<pre>') + 5
        retend = ret.index('</pre>')
        ret = ret[retstart:retend]
    return ret


"""
def findNextSpeaker(contents):
	ret = float('inf')
	while (ret == float('inf') and len(contents) > 0):
		spotToCheck = float('inf')
		endSpot = float('inf')
		findEndBreak = contents.find("____________________")
		if findEndBreak != -1:
		  endSpot = findEndBreak
		prefixes = ["Mr. ", "Mrs. ", "Ms. "]
		if (endSpot == float('inf') and "Mr. " not in contents and "Mrs. " not in contents and "Ms. " not in contents):
			break
		for prefix in prefixes:
			temp = contents.find(prefix)
			if temp >= 0 and temp < spotToCheck:
				spotToCheck = temp + len(prefix)
		print(spotToCheck)
		if spotToCheck != float('inf'):
			contents = contents[spotToCheck:]
			if not (contents[spotToCheck+1].isupper() and contents[spotToCheck+3].isupper()):
			  spotToCheck = float('inf')
		ret = min(endSpot, spotToCheck)
	return ret
"""


def cleanForSpeeches(contents):
    record = ""
    recordList = []
    while (True):
        if ("2018\n" not in contents and "2019\n" not in contents):
            break
        else:
            spotToCheck = float('inf')
            prefixes = ["2018\n", "2019\n"]
            for prefix in prefixes:
                temp = contents.find(prefix)
                if temp >= 0 and temp < spotToCheck:
                    spotToCheck = temp + len(prefix)

            # TODO: Account for names like McGOVERN and LaMALFA
            #if (contents[spotToCheck + 1].isupper() and contents[spotToCheck + 3].isupper()):
            contents = contents[spotToCheck:]
                #continue
            #else:
            endSpot = float('inf')
            findEndBreak = contents.find("____________________")
            if findEndBreak != -1:
                endSpot = findEndBreak

            if endSpot == float('inf'):
                endSpot = len(contents)
            recordList.append(contents[:endSpot])
            record += contents[:endSpot]
            contents = contents[endSpot:]
    writer = open("writer.txt", 'a')
    for r in recordList:
        for ch in r:
            writer.write(ch)
        writer.write("\n\n\n")
    return record

    """
    spotToCheck = findNextSpeaker(contents)
    temp = contents[spotToCheck]
    endSpot = findNextSpeaker(temp) + spotToCheck
    print(spotToCheck)
    print(endSpot)
    record += contents[spotToCheck:endSpot]
    contents = contents[endSpot:]
return record

"""


main()
