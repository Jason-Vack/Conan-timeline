# coding=utf-8
import re
import requests


f = open("TokyoWeather.txt", "w")
m = 'http://weather.goo.ne.jp/past/662/'
n = '00/'
i = 1
j = 1994
urllist = []

while j < 1995:
    while i < 13:
        if i < 10:
            y = m + str(j) + '0' + str(i) + n
        else:
            y = m + str(j) + str(i) + n
        i += 1
        urllist.append(y)
    j += 1
    i = 1

for x in urllist:
    totalhigh = 0.0
    totallow = 0.0
    temp3 = requests.get(x)
    temp = temp3.text
    highweather = re.findall("red\">-?[0-9][0-9]?\.?[0-9]?", temp)
    for y in highweather:
        if y[5] == '-':
            if len(y) == 7:
                totalhigh -= float(y[6])
            elif len(y) == 9:
                totalhigh -= float(y[6:9])
            else:
                totalhigh -= float(y[6:10])
        else:
            if len(y) == 6:
                totalhigh += float(y[5])
            elif len(y) == 8:
                totalhigh += float(y[5:8])
            else:
                totalhigh += float(y[5:9])
    avghigh = totalhigh / len(highweather)
    lowweather = re.findall("blue\">-?[0-9][0-9]?\.?[0-9]?", temp)
    for y in lowweather:
        if y[6] == '-':
            if len(y) == 8:
                totallow -= float(y[7])
            elif len(y) == 10:
                totallow -= float(y[7:10])
            else:
                totallow -= float(y[7:11])
        else:
            if len(y) == 7:
                totallow += float(y[6])
            elif len(y) == 9:
                totallow += float(y[6:9])
            else:
                totallow += float(y[6:10])
    avglow = totallow / len(lowweather)
    print ("%.2f %.2f" % (avghigh, avglow))
    print >> f, ("%.2f %.2f" % (avghigh, avglow))

f.close()
