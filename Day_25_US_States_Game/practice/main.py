import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))

data_dic = data.to_dict()
# print(data_dic)

temp_list = data["temp"].to_list()
# print(temp_list)

# avergae_temp = sum(temp_list) / len(temp_list)
# print(avergae_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday" ]
# monday_temp = monday.temp[0]
# print(monday_temp)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Gray = len(data[data["Primary Fur Color"] == "Gray"])
Red = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])
print(Gray)
print(Red)
print(Black)

data_dic = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [Gray,Red,Black]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")