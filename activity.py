__author__ = 'saba'
import csv as csv
import numpy as np
import sys
sys.path.append('/Library/Python/2.7/site-packages/pyparsing-2.0.1-py2.7.egg')
import pyparsing
import matplotlib.pyplot as plotter
import matplotlib.pyplot as plt
import sklearn.neighbors as ne
import math
import scipy as sc

csvFiles = ['activity9.csv', 'activity11.csv', 'activity17.csv', 'activity18.csv', 'activity22.csv', 'activity23.csv',
            'activity24.csv', 'activity25.csv', 'activity26.csv', 'activity27.csv']
typeDay = ['day', 'weekend', 'weekend', 'weekend', 'day', 'day', 'weekend', 'weekend', 'day', 'day']

anomalies = ['activity10.csv', 'activity28.csv']
anomaliesType = ['weekend', 'day']

dayNumber = 0
allData = []

#######################################################
for file in csvFiles:
    dayRow = []
    csvObject = csv.reader(open(file, 'rt'))
    for row in csvObject:
        if row[4] == "WEB":
            dayRow.append(float(row[5]))
    allData.append(dayRow)
    dayNumber += 1

allData = np.array(allData)

anomalyData = []
anomalyNumber = 0
for anomaly in anomalies:
    anomalyRow = []
    csvObject = csv.reader(open(anomaly, 'rt'))
    for row in csvObject:
        if row[4] == "WEB":
            anomalyRow.append(float(row[5]))
    anomalyData.append(anomalyRow)
    anomalyNumber += 1

anomalyData = np.array(anomalyData)
#each row in the data corresponds to a row
timePoints = range(0, allData.shape[1])

#######################################################

normalizedData = []
for day in range(0, dayNumber):
    minR = allData[day, :].min()
    maxR = allData[day, :].max()
    normRow = (allData[day, :] - minR)/(maxR-minR)
    normalizedData.append(normRow)

normalizedData = np.array(normalizedData)

normAnomalyData = []
for anomalyDay in range(0, anomalyNumber):
    anomalyData[anomalyDay, :] = anomalyData[anomalyDay, :]
    minR = anomalyData[anomalyDay, :].min()
    maxR = anomalyData[anomalyDay, :].max()
    normRow = (anomalyData[anomalyDay, :] - minR)/(maxR-minR)
    normAnomalyData.append(normRow)

normAnomalyData = np.array(normAnomalyData)

######################################################

weekendCoeffs = []
dayCoeffs = []

for day in range(0, dayNumber):
    if typeDay[day] == 'weekend':
        weekendCoeffs.append(np.polyfit(timePoints, normalizedData[day, :], 5))
    else:
        dayCoeffs.append(np.polyfit(timePoints, normalizedData[day, :], 5))

weekendCoeffs = np.array(weekendCoeffs)
dayCoeffs = np.array(dayCoeffs)

avgWeekendCoeffs = np.average(weekendCoeffs, axis=0)
polyWeekend = np.poly1d(avgWeekendCoeffs)
polyYsWeekend = polyWeekend(timePoints)

avyDayCoeffs = np.average(dayCoeffs, axis=0)
polyDay = np.poly1d(avyDayCoeffs)
polyYsDay = polyDay(timePoints)

################################################################


for day in range(0, dayNumber):
    if typeDay[day] == 'weekend':
        fig = plt.figure(1)
        #fig.suptitle('Weekend Activity')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Active User Count', fontsize=18)
    else:
        fig = plt.figure(2)
        #fig.suptitle('Week Day Activity')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Active User Count', fontsize=18)
    plt.plot(timePoints, normalizedData[day, :], 'o')

fig = plt.figure(5)
fig.suptitle('Estimated Weekend Activity')
plt.xlabel('Time', fontsize=18)
plt.ylabel('Active User Count', fontsize=18)
plt.plot(timePoints, polyYsWeekend, 'black')

fig = plt.figure(6)
fig.suptitle('Estimated Week day Activity')
plt.xlabel('Time', fontsize=18)
plt.ylabel('Active User Count', fontsize=18)
plt.plot(timePoints, polyYsDay, 'black')

for anomalyDay in range(0, anomalyNumber):
    if anomaliesType[anomalyDay] == 'day':
        fig = plt.figure(3)
        fig.suptitle("New Week Day Activity")
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Active User Count', fontsize=18)
    else:
        fig = plt.figure(4)
        fig.suptitle("New Week End Activity")
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Active User Count', fontsize=18)
    plt.plot(timePoints, normAnomalyData[anomalyDay, :], 'o')

plt.figure(4)
plt.plot(timePoints, polyYsWeekend)

plt.figure(3)
plt.plot(timePoints, polyYsDay)

euclideanDay = np.sqrt((normAnomalyData[1, :] - polyYsDay)**2)
euclideanWeekend = np.sqrt((normAnomalyData[0, :] - polyYsWeekend)**2)


plt.figure(3)
plt.plot(timePoints, euclideanDay)

plt.figure(4)
plt.plot(timePoints, euclideanWeekend)

plt.show()
#print(normalizedData.shape)
#print(anomalyData[0, :]/maxDay)



