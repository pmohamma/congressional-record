import os
import re

def main():
    rootdir = 'C:/Users/pouya\python-projects\congressional-record\congressionalrecord\output'
    writer = open("writer.txt", 'w')
    writer.close()
    dirtyWriter = open("dirtyWriter.txt", 'w')
    dirtyWriter.close()
    speakerDict = {}
    numberOfDays = {"ignore this day"}

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.htm'):
                fname = subdir + '\\' + file
                numberOfDays.add(subdir)
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
                contentList = cleanForSpeeches(contents)
                for r in contentList:
                    nameEnd = findNth(r, ".", 2)
                    name = r[0:nameEnd]
                    if name not in speakerDict:
                        speakerDict[name] = list()
                    speakerDict[name].append(r[nameEnd:])

    numberOfSpeeches = 0
    for speaker in speakerDict:
        print(speaker + ":    " + str(len(speakerDict[speaker])))
        numberOfSpeeches += len(speakerDict[speaker])
        #for speech in speakerDict[speaker]:
            #print(speech + "\n\n")
    print(str(numberOfSpeeches) + " speeches over " + str(len(numberOfDays) - 1) + " days")

def cleanContents(contents):
    bodystart = contents.index('<body>') + 6
    bodyend = contents.index('</body>')
    ret = contents[bodystart:bodyend]
    if (ret.index("<pre>") != -1):
        retstart = ret.index('<pre>') + 5
        retend = ret.index('</pre>')
        ret = ret[retstart:retend]
    return ret


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
            pageLoc = contents.find("[[Page ")
            while (pageLoc != -1):
                pageFinder = re.search('[[][[][P][a][g][e][ ].[0-9]+]]', contents)
                page = pageFinder.group(0)
                contents = contents.replace(page, '')
                pageLoc = contents.find("[[Page ")
                print(pageLoc)
            if (contents[3:4] == 'M'): #checks for if it is a speaker or a formality
                recordList.append(contents[:endSpot])
                record += contents[:endSpot]
                contents = contents[endSpot:]
    writer = open("writer.txt", 'a')
    for r in recordList:
        for ch in r:
            writer.write(ch)
        writer.write("\n\n\n")
    return recordList

def findNth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

main()
