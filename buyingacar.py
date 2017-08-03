def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    capital = startPriceOld
    remainder = capital - startPriceNew
    month = 0
    percentLossByMonth = percentLossByMonth/100
    while capital < startPriceNew:
        month += 1
        if month%2 == 0:
            percentLossByMonth += 0.005
        startPriceOld = startPriceOld - (startPriceOld*percentLossByMonth)
        startPriceNew = startPriceNew - (startPriceNew*percentLossByMonth)
        capital = startPriceOld + (savingperMonth * month)
        remainder = capital - startPriceNew
    return [month, int(round(remainder))]

print(nbMonths(2000, 8000, 1000, 1.5))
