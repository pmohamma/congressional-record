import json

def main(oldFile, newFile):
    f = open(oldFile, 'r')
    writer = open(newFile, 'w')
    oldData = json.load(f)
    f.close()

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
        if not (startYear in yearRange or endYear not in yearRange):
            print(name)
            continue
        politician = {}
        politician['name'] = oldData[i]['name']
        politician['terms'] = oldData[i]['terms']

        if "Engel" in name:
            print("start year: " + str(startYear))
            print("end year: " + str(endYear))

        if startYear in yearRange:
            rangeEnd = min(2019, endYear)
            for ny in range(startYear, rangeEnd):
                newData[str(ny)][name] = politician
        elif endYear in yearRange or endYear > 2019:
            rangeStart = max(startYear, 2005)
            rangeEnd = min(endYear, 2020)
            for ny in range(rangeStart, rangeEnd):
                newData[str(ny)][name] = politician


    json.dump(newData, writer)

    writer.close()


main("legislators-historical.json", "historicalLegislators.json")
main("legislators-current.json", "currentLegislators.json")