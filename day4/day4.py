# For example:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). 
# Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! 
# That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

# Take a seat in the large pile of colorful cards. How many points are they worth in total?


#todo pobranie danych z pliku tekstowego day4.txt
#todo rozdzielnie danych na dwa zbiory tj liczb wygrywajacych i liczb wylosowanych + usuniecie numeru karty
#to do sprawdzenie czy w danej grze liczby wybgrywajace pokrywaja sie z liczbami wylosowanymi
#to do obliczenie sily danego losu w grze i dodoanie go do zbioru liczb
#poodsumwoanie i wyswietlenie informaccji o sile wszystkich losow

import os

# Sprawdź bieżący katalog roboczy
print(os.getcwd())

# Ustaw bieżący katalog roboczy na katalog skryptu
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('day4.txt', 'r') as file:
    data = file.readlines()

points = []

for line in data:
    # Usunięcie tekstu dotyczącego numeru karty, czyli wszystko przed ":"
    win_part, selected_no = line.split(': ')[1].split('|')

    # Podzielenie uzyskanego zbioru na dwie osobne listy liczb
    win_numbers = [int(num) for num in win_part.split()]
    selected_numbers = [int(num) for num in selected_no.split()]

    # Obliczenie liczby wspólnych liczb między win_numbers a selected_numbers
    common_numbers = set(win_numbers) & set(selected_numbers)
    common_count = len(common_numbers)

    print(common_count)
    # Obliczenie liczby punktów dla danej karty
    card_points = 2 ** (common_count - 1) if common_count > 0 else 0

    # Dodanie punktów danej karty do ogólnej puli punktów
    points.append(card_points)

# Wyświetlenie wyniku
print("Punkty:", points)
print("Suma punktów:", sum(points))