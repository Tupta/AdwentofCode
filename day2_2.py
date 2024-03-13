import pandas as pd

# Wczytanie danych z pliku tekstowego
df = pd.read_csv('day2.txt', header=None, names=['Game', 'Cubes'])

# Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
red_limit = 12
green_limit = 13
blue_limit = 14

# Funkcja sprawdzająca czy gra jest możliwa
def is_game_possible(cubes_data):
    cubes = cubes_data.split(', ')
    for cube in cubes:
        color, count = cube.split()
        count = int(count)
        if (color == 'red' and count > red_limit) or \
           (color == 'green' and count > green_limit) or \
           (color == 'blue' and count > blue_limit):
            return False
    return True

# Dodanie kolumny z informacją czy gra jest możliwa
df['Is Possible'] = df['Cubes'].apply(is_game_possible)

# Suma numerów ID gier możliwych
sum_possible_games = df[df['Is Possible']]['Game'].sum()

print("Suma numerów ID gier możliwych:", sum_possible_games)
