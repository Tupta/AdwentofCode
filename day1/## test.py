## test


# For example:

data2 = ['abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet', 'one4two']

#########################################
# Tworzymy słownik mapujący słowa na ich wartości liczbowe
word_values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# Lista danych wejściowych
data2 = ['abc2', 'pqr3stutwonine8vwx', 'a1b2c3d4e5f', 'treb7uchet', 'one4two']

# Funkcja do przekształcenia liter na liczby w oparciu o słownik word_values
def convert_word_to_number(word):
    # Jeżeli słowo znajduje się w słowniku word_values, zwróć jego wartość liczbową, w przeciwnym razie zwróć 0
    return word_values.get(word, 0)

# Przetwarzamy elementy listy data2
for i, element in enumerate(data2):
    word = ''
    new_element = ''
    for char in element:
        if char.isalpha():  # Jeżeli znak jest literą, dodaj go do aktualnie przetwarzanego słowa
            word += char
        else:
            if word.lower() in word_values:  # Jeżeli słowo jest w słowniku, zamień je na jego wartość liczbową
                new_element += str(word_values[word.lower()])  # Dodaj wartość liczbową do nowego elementu
            else:
                new_element += word  # Jeżeli słowo nie ma wartości liczbowej, dodaj je bez zmian
            new_element += char  # Dodaj znak (np. cyfrę) do nowego elementu
            word = ''  # Wyzeruj słowo po przetworzeniu
    if word.lower() in word_values:  # Sprawdź, czy ostatnie słowo na końcu elementu wymaga konwersji
        new_element += str(word_values[word.lower()])  # Dodaj wartość liczbową do nowego elementu
    else:
        new_element += word  # Jeżeli słowo nie ma wartości liczbowej, dodaj je bez zmian
    data2[i] = new_element  # Zaktualizuj element listy

print(data2)
        




########################################
data = [11, 12, 13, 14, 15, 16, 17, 18, 19]

allnumbers = []
for element in data:
    number_str = ''.join(char for char in element if char.isdigit())
    if number_str:
            allnumbers.append(int(number_str))

print(allnumbers)

twoDigitNumbers = []
for number in allnumbers:
    if number <= 9:
            newnumber = number * 10 + number
    else:
      firstdigit = int(str(number)[0])
      secondigit = int(str(number)[-1])
      newnumber = firstdigit *10 + secondigit
    twoDigitNumbers.append(newnumber)
print(twoDigitNumbers)