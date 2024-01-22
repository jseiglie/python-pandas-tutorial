import pandas as pd

# # 2
# print("Hello World")
# import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)
# 3
# ages = [23,45,7,34,6,63,36,78,54,34]
# serie = pd.Series(ages)
# print(serie)

# 4

# print(pd.date_range("05-01-2021", "05-12-2021"))

# my_series = pd.Series([2, 4, 6, 8, 10])
# print(my_series.apply(lambda x: x/2))

# 5

# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]

# df = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
# print(df)

# newData = [
#     { 
#         "brand": "Toyota", 
#         "make": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "make": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porche", 
#         "make": "Cayenne",
#         "color": "White"
#     }
# ]
# newData.append({"brand": "Tesla", 
#         "make": "Model S",
#         "color": "Red"})

# newdf = pd.DataFrame(newData, columns=["brand", "make", "color"])
# print(newdf)

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# # print(data_frame.iloc[133, 6])

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# # print(data_frame.head(3))
# # print(data_frame.tail(3))

# print(data_frame[['Name', 'Type 1']][0:10])
# print(data_frame.loc[data_frame['Attack']>80])

# print(len(data_frame.loc[data_frame["Legendary"]==True]))

# 6

# dataSet = pd.read_csv(".learn/assets/us_baby_names_right.csv")

# print(dataSet.head(5))
# dataSet = dataSet.drop("Unnamed: 0", axis=1)
# print(dataSet.head(5))

# print(dataSet["Gender"].value_counts())

# print(len(dataSet.groupby("Name").sum()))