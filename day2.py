# Maksymalna liczba kolorowych kul dla każdego koloru
max_balls = {'blue': 12, 'red': 13, 'green': 14}

# Otwarcie pliku tekstowego do odczytu
with open("nazwa_pliku.txt", "r") as file:
    for i, line in enumerate(file, 1):
        # Podział linii na nazwę gry i wyniki poszczególnych losowań
        draws = line.strip().split(";")
        # Inicjalizacja listy wyników gry
        game_results = []
        # Przetworzenie kolejnych losowań
        for draw in draws:
            # Podział losowania na poszczególne kule i ich ilości
            balls = draw.strip().split(", ")
            # Sprawdzenie, czy ilości kulek nie przekraczają maksymalnej liczby
            for ball in balls:
                color, count = ball.split()
                if int(count) > max_balls[color]:
                    print(f"Game {i} couldn't be played due to too many {color} balls.")
                    break
