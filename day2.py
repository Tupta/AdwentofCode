# example_list = ["Game 1: 9 red, 5 blue, 6 green; 6 red, 13 blue; 2 blue, 7 green, 5 red",
#                 "Game 2: 6 red, 2 green, 2 blue; 12 green, 11 red, 17 blue; 2 blue, 10 red, 11 green; 13 green, 17 red; 15 blue, 20 red, 3 green; 3 blue, 11 red, 1 green",
#                 "Game 3: 20 green, 1 blue, 7 red; 20 green, 7 blue; 18 red, 8 green, 3 blue; 7 red, 6 blue, 11 green; 11 red, 6 blue, 16 green"]

# # Inicjalizacja listy, która będzie przechowywać numery ID gier, które byłyby możliwe
# possible_games = []

# # Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
# red_limit = 12
# green_limit = 13
# blue_limit = 14

# for game in example_list:
#     game_id, cubes_data = game.strip().split(': ')
#     game_id = game_id.replace("Game ", "")
#     print(game_id)
#     cubes_sets = cubes_data.split(';')
#     for cubes_set in cubes_sets:
#         cubes = cubes_set.split(', ')
#         print(cubes)
        
        
        
example_list = ["Game 1: 9 red, 5 blue, 6 green; 6 red, 13 blue; 2 blue, 7 green, 5 red",
                "Game 2: 6 red, 2 green, 2 blue; 12 green, 11 red, 17 blue; 2 blue, 10 red, 11 green; 13 green, 17 red; 15 blue, 20 red, 3 green; 3 blue, 11 red, 1 green",
                "Game 3: 20 green, 1 blue, 7 red; 20 green, 7 blue; 18 red, 8 green, 3 blue; 7 red, 6 blue, 11 green; 11 red, 6 blue, 16 green"]

# Inicjalizacja listy, która będzie przechowywać numery ID gier, które byłyby możliwe
possible_games = []

# Ograniczenia dotyczące liczby kostek czerwonych, zielonych i niebieskich
red_limit = 12
green_limit = 13
blue_limit = 14

for game in example_list:
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