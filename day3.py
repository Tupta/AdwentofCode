# Wczytanie danych z pliku tekstowego
with open('day3.txt', 'r') as file:
    engine_schematic = file.readlines()

# Inicjalizacja zbioru, który będzie przechowywać unikalne numery części
part_numbers = set()

# Przechodzimy przez każdy wiersz schematu silnika
for row in engine_schematic:
    # Usuwamy białe znaki z wiersza i dzielimy go na części oddzielone kropką
    parts = row.strip().split('.')
    # Iterujemy przez części, zaczynając od drugiej, ponieważ pierwsza część nie może tworzyć liczby z poprzedniego wiersza
    for part in parts[1:]:
        # Sprawdzamy, czy znak przylega do każdej cyfry tylko raz
        unique_digits = set(part)
        if len(unique_digits) == len(part):
            # Jeśli tak, to znaczy, że każda cyfra przylega tylko raz
            # Przetwarzamy tę część i dodajemy każdą liczbę do zbioru part_numbers
            for char in part:
                if char.isdigit():
                    number = int(char)
                    for next_char in part[part.index(char)+1:]:
                        if next_char.isdigit():
                            number = number * 10 + int(next_char)
                        else:
                            break
                    part_numbers.add(number)

# Sumujemy wszystkie unikalne numery części
total_sum = sum(part_numbers)

print("Suma wszystkich numerów części:", total_sum)

anserw is toooo loooooww