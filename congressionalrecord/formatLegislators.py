import json
from stateAbbreviations import getStateAbbreviations

def main(oldFile, newFile):
    f = open(oldFile, 'r')
    writer = open(newFile, 'w')
    oldData = json.load(f)
    f.close()

    yearRange = range(2005, 2020)
    newData = {}
    for i in yearRange:
        newData[str(i)] = {}

    stateAbbreviations = getStateAbbreviations()

    for i in range(len(oldData)):
        if 'middle' in oldData[i]["name"].values():
            name = (oldData[i]["name"]['first']) + " " + (oldData[i]["name"]['middle']) + " " + (oldData[i]["name"]['last'])
        else:
            name = (oldData[i]["name"]['first']) + " " + (oldData[i]["name"]['last'])
        #name = oldData[1]["name"]["last"]
        name = stripForLetters(name)

        keyName = name.split(" ")[-1].lower()
        #print(name)

        startDate = oldData[i]['terms'][0]['start']
        startYear = int(startDate[:4])
        endDate = oldData[i]['terms'][-1]['end']
        endYear = int(endDate[:4])
        endYear = stripForNumbers(endYear)

        if (startYear not in yearRange):
            if (endYear not in yearRange and endYear < 2019):
                continue
        politician = {}
        politician['name'] = oldData[i]['name']
        politician['terms'] = oldData[i]['terms']

        if startYear in yearRange:
            rangeEnd = min(2020, endYear)
            for ny in range(startYear, rangeEnd):
                if keyName in newData[str(ny)]:
                    oldPolitician = newData[str(ny)][keyName]
                    oldPolState = (stateAbbreviations[oldPolitician['terms'][0]['state']]).lower()
                    newData[str(ny)][keyName + " of " + oldPolState] = oldPolitician
                    newData[str(ny)].pop(keyName)
                    newPolState = (stateAbbreviations[politician['terms'][0]['state']]).lower()
                    newData[str(ny)][keyName + " of " + newPolState] = politician
                    print(keyName + " of " + oldPolState)
                    print(keyName + " of " + newPolState)
                    print('\n\n')

                else:
                    newData[str(ny)][keyName] = politician
        elif endYear in yearRange or endYear > 2019:
            rangeStart = max(startYear, 2005)
            rangeEnd = min(endYear, 2020)
            for ny in range(rangeStart, rangeEnd):
                if keyName in newData[str(ny)]:
                    newData[str(ny)][keyName + " " + name] = politician
                else:
                    newData[str(ny)][keyName] = politician


    json.dump(newData, writer)

    writer.close()


def stripForNumbers(phrase):
    word = ""
    for ch in str(phrase):
        if ch.isnumeric() or ch == " ":
            word += ch.lower()
    return int(word)

def stripForLetters(phrase):
    word = ""
    for ch in phrase:
        if ch.isalpha() or ch == " " or ch == "-" or ch == "'":
            word += ch.lower()
    return word

#main("legislators-historical.json", "historicalLegislators.json")
main("legislators-current.json", "currentLegislators.json")