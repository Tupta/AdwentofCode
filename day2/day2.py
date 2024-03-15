# advent of code day 2

# Game data is in text file day2.txt
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 1
# 3 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?


# #todo odczytanie z danych pliku tekstowego "day2" i wrzucenie ich do zmiennej, kolejne gry jako kolejne linie tekstu
# #todo rozdzielenie numeru gry od wyników gry usuniecie słowa "Game" dla łątiwejszego przetwarzania numeru gry
# #todo rozdzielenie wyników gier na poszczegolne elementy tak by mozna bylo porownac elementy pojedynczej gry z max iloscia kolorowych kosci
# #todo sprawdzenie czy kazdy z elementow wylosowanych w danej grze nie przekracza limitu ilosciowego jezeli nie dodanie numeru gry do osobnego zbioru
# #todo zsumowanie wszystkich numerów oznaczajacych gry mozliwe do przeprowadzenia i podanie wyniku tej sumy.

# Wczytanie danych z pliku tekstowego
with open('day2.txt', 'r') as file:
    games_data = file.readlines()

# Inicjalizacja listy, która będzie przechowywać numery ID gier, które byłyby możliwe
possible_games = []


# Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
red_limit = 12
green_limit = 13
blue_limit = 14

for game in games_data:
    game_id, cubes_data = game.strip().split(': ')
    game_id = game_id.replace("Game ", "")
    cubes_sets = cubes_data.split(';')
    is_valid_game = True
    
    for cubes_set in cubes_sets:
        cubes = cubes_set.split(', ')
        for cube in cubes:
            count, color = cube.split()
            count = int(count)
            if color == "red" and count > red_limit:
                is_valid_game = False
            elif color == "green" and count > green_limit:
                is_valid_game = False
            elif color == "blue" and count > blue_limit:
                is_valid_game = False
    
    if is_valid_game:
        possible_games.append(game_id)

print("Possible games:", possible_games)

total_possible_games = sum(int(game_id) for game_id in possible_games)

print("Suma numerów porzadkowych możliwych gier:", total_possible_games)