def sum_calibration_values(file_path):
    # Słownik mapujący słowa na ich wartości liczbowe
    word_values = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # Otwieramy plik tekstowy
    with open(file_path, "r") as file:
        # Odczytujemy linie z pliku
        lines = file.readlines()

    # Inicjalizujemy sumę dwucyfrowych liczb
    sum_of_two_digit_numbers = 0

    # Iterujemy przez każdą linię w pliku
    for line in lines:
        # Tworzymy nową linię, w której zamieniamy słowa kluczowe na ich wartości liczbowe
        for word, value in word_values.items():
            line = line.replace(word, value)
        
        # Usuwamy wszystkie znaki, które nie są cyframi ani spacjami
        line = ''.join(char if char.isdigit() or char.isspace() else ' ' for char in line)

        # Rozdzielamy linię na pojedyncze liczby, ignorując spację
        numbers = line.split()

        # Iterujemy przez liczby w linii
        for number in numbers:
            # Sprawdzamy czy liczba jest dwucyfrowa
            if len(number) == 2:
                sum_of_two_digit_numbers += int(number)

    return sum_of_two_digit_numbers

file_path = "C:\\Users\\Tupta\\Desktop\\AdwentofCode\\day1\\day1.txt"
result = sum_calibration_values(file_path)
print("Sum of calibration values:", result)
