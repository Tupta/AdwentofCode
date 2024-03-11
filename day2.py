# Wczytanie danych z pliku tekstowego
with open('day2.txt', 'r') as file:
    games_data = file.readlines()

# Inicjalizacja listy, która będzie przechowywać numery ID gier, które byłyby możliwe
possible_games = []

# Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
red_limit = 12
green_limit = 13
blue_limit = 14

# Iteracja przez dane każdej gry
for game_data in games_data:
    # Podzielenie danych gry na ID gry i zbiory kostek
    game_id, cubes_data = game_data.strip().split(': ')
    cubes_sets = cubes_data.split('; ')

    # Inicjalizacja flagi, która będzie śledzić, czy gra jest możliwa
    is_possible = True

    # Iteracja przez zbiory kostek w danej grze
    for cubes_set in cubes_sets:
        # Podzielenie zbioru kostek na kolor i liczbę
        color, count = cubes_set.split()
        count = int(count)

        # Sprawdzenie, czy liczba kostek danego koloru przekracza limit
        if (color == 'red' and count > red_limit) or \
           (color == 'green' and count > green_limit) or \
           (color == 'blue' and count > blue_limit):
            is_possible = False
            break

    # Dodanie numeru ID gry do listy, jeśli gra jest możliwa
    if is_possible:
        possible_games.append(int(game_id))

# Obliczenie sumy numerów ID gier, które byłyby możliwe
sum_possible_games = sum(possible_games)

# Wyświetlenie wyniku
print("Suma numerów ID gier możliwych:", sum_possible_games)
