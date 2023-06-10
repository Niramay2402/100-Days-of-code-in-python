import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
N_ofGray = 0
N_ofCinnamon = 0
N_ofBlack = 0

for x in data["Primary Fur Color"]:
    if x == "Gray":
        N_ofGray += 1
    elif x == "Black":
        N_ofBlack += 1
    elif x == "Cinnamon":
        N_ofCinnamon += 1
    else:
        pass

# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"]

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [N_ofGray, N_ofCinnamon, N_ofBlack]
}

nCsv = pandas.DataFrame(data_dict)
nCsv.to_csv("Squirrel_count.csv")



