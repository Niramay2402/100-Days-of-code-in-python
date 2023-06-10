import pandas

data = pandas.read_csv("weather_data.csv")

# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# data_list = data["temp"].to_list()
# # print(data_list)
#
# # avg = float(sum(data_list)/len(data_list))
# # print(avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get Columns
# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# M_temp = int(monday.temp)
# M_temp_F = (M_temp * 9/5) + 32
# print(M_temp_F)

# CREATE DATAFRAME

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 39]
}

data = pandas.DataFrame(data_dict)
data.to_csv("New_data.csv")
