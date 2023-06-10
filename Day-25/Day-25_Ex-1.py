# with open("weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

#
# import csv
#
# with open("weather_data.csv") as datafile:
#
#     data = csv.reader(datafile)
#     # print(data)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# intro to pandas...
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
