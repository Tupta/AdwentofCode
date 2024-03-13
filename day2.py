# Wczytanie danych z pliku tekstowego
with open('day2.txt', 'r') as file:
    games_data = file.readlines()

# Inicjalizacja listy, która będzie przechowywać numery ID gier, które byłyby możliwe
possible_games = []

# Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
red_limit = 12
green_limit = 13
blue_limit = 14

# Funkcja sprawdzająca, czy gra jest możliwa
def is_game_possible(cubes_data):
    cubes = cubes_data.split(', ')
    for cube in cubes:
        color, count = cube.split()
        if (color == 'red' and int(count) > red_limit) or \
           (color == 'green' and int(count) > green_limit) or \
           (color == 'blue' and int(count) > blue_limit):
            return False
    return True

# Iteracja przez dane każdej gry
for game_data in games_data:
    # Podzielenie danych gry na ID gry i zbiory kostek
    game_id, cubes_data = game_data.strip().split(': ')
    game_id = game_id.replace('Game ', '')  # Usunięcie słowa "Game" z numeru ID gry

    cubes_sets = cubes_data.split('; ')

    # Inicjalizacja flagi, która będzie śledzić, czy gra jest możliwa
    is_possible = True

    # Iteracja przez zbiory kostek w danej grze
    for cubes_set in cubes_sets:
        # Sprawdzenie, czy gra jest możliwa
        if not is_game_possible(cubes_set):
            is_possible = False
            break

    # Dodanie numeru ID gry do listy, jeśli gra jest możliwa
    if is_possible:
        possible_games.append(int(game_id))

# Obliczenie sumy numerów ID gier, które byłyby możliwe
sum_possible_games = sum(possible_games)

# Wyświetlenie wyniku
print("Suma numerów ID gier możliwych:", sum_possible_games)
