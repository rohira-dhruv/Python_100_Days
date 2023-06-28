# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# temp_list = data["temp"].to_list()
# # print(sum(temp_list) / len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((9 / 5 * monday.temp) + 32)
#
# # Create a DataFrame from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_sheet.csv")

import pandas

data = pandas.read_csv("resources/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./resources/squirrel_count.csv")
