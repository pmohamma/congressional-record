import json

def main(oldFile, newFile):
    f = open(oldFile, 'r')
    writer = open(newFile, 'w')
    oldData = json.load(f)

    yearRange = range(2005, 2020)
    newData = {}
    for i in yearRange:
        newData[str(i)] = {}

    for i in range(len(oldData)):
        if 'middle' in oldData[i]["name"].values():
            name = (oldData[i]["name"]['first']) + " " + (oldData[i]["name"]['middle']) + " " + (oldData[i]["name"]['last'])
        else:
            name = (oldData[i]["name"]['first']) + " " + (oldData[i]["name"]['last'])
        startDate = oldData[i]['terms'][0]['start']
        startYear = int(startDate[:4])
        endDate = oldData[i]['terms'][-1]['end']
        endYear = int(endDate[:4])
        if (startYear not in yearRange) and (endYear not in yearRange):
            continue
        politician = {}
        politician['name'] = oldData[i]['name']
        politician['terms'] = oldData[i]['terms']

        if startYear in yearRange:
            rangeEnd = min(2019, endYear)
            for ny in range(startYear, rangeEnd):
                newData[str(ny)]['name'] = politician
        elif endYear in yearRange:
            rangeStart = max(startYear, 2005)
            for ny in range(rangeStart, endYear):
                newData[str(ny)][name] = politician


    json.dump(newData, writer)

    f.close()
    writer.close()


main("legislators-historical.json", "historicalLegislators.json")
main("legislators-current.json", "currentLegislators.json")