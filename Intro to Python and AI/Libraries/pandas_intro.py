import pandas as pd

my_dataframe = pd.DataFrame(
    {
        "Name": ("Rei", "Alexis", "Riley", "Anna", "Miya", "Luke"),
        "Favorite Color": ("Green", "Yellow", "Purple", "Orange", "Blue", "Red"),
        "Age": (13, 15, 8, 10, 14, 9),
        "Favorite Candy": ("Snickers", "Hershey's", "Gummy Words", "Candy Corn", "Kit Kats", "Sour Patch Kids")
    }
)

test_data = my_dataframe.drop(['Favorite Color', 'Favorite Candy'], axis=1)
print(my_dataframe)
print(test_data)
penguins = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
penguins = penguins.dropna()
print(penguins['island'])
print(penguins[14:23])
penguins = penguins.sort_values(by="flipper_length_mm", ascending=False)
penguins = penguins.sort_values(by="body_mass_g", ascending=False)

print(penguins.head())
