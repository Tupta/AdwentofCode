
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

print(sum(possible_games))