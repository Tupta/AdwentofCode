####day 1######

# calibration document consists of lines of text; each line originally contained a specific calibration value. 
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
#to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

#todo odczytanie z danych pliku tekstowego "day1" wszystkich liczb w kolejnych liniach i wpisanie ich jako kolejnych elementów słownika
#todo jeżeli jakaś liczba jest jednocyfrowa należy utworzyć z niej liczbę dwucyfrową poprzez jej zdublowanie
#todo stowrzenie nowego słownika zawierającego liczby utworzone tylko z pierwszej i ostatniej liczby w poprzendim słowniku
#todo zsumowanie wszystkich liczb dwucyfrowych w słowniku i podanie wyniku tej sumy.

data = open("C:\\Users\\Tupta\\Desktop\\AdwentofCode\\day1\\day1.txt", "r")
#print(data.read())

allData = []

for line in data:
    allData.append(line.strip())
    
print(allData) 
#Tworzymy słownik mapujący słowa na ich wartości liczbowe
word_values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# Funkcja do przekształcenia liter na liczby w oparciu o słownik word_values
def convert_word_to_number(word):
    # Jeżeli słowo znajduje się w słowniku word_values, zwróć jego wartość liczbową, w przeciwnym razie zwróć 0
    return word_values.get(word, 0)

# Przetwarzamy elementy listy data2
for i, element in enumerate(allData):
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
    allData[i] = new_element  # Zaktualizuj element listy

print(allData)



print(f' ilosc elementow w alldata jest rowna {len(allData)}')

#stworzenie listy zawierającej tylko liczby
allNumbers = []
for element in allData:
        lineNumber = ''.join(char for char in element if char.isdigit())
        if lineNumber:
            allNumbers.append(int(lineNumber))

print(allNumbers)
print(f' ilosc elementow w allNumbers jest rowna {len(allNumbers)}')
print(f' ilosc elementow w alldata jest rowna {len(allData)}')

print()
print()

#tworzenie listy zawierającej tylko dwucyfrowe liczby
twoDigitNumbers = []
for number in allNumbers:
    if number <= 9:
        newnumber = number * 10 + number
    else:
         firstDigit = int(str(number)[0])
         secondDigit = int(str(number)[-1])
         newnumber = firstDigit * 10 + secondDigit
    twoDigitNumbers.append(newnumber)

print(twoDigitNumbers)
print()

print(f' ilosc elementow w allNumbers jest rowna {len(allNumbers)}')
print(f' ilosc elementow w alldata jest rowna {len(allData)}')
print(f' ilosc elementow w alldata jest rowna {len(twoDigitNumbers)}')

coordinates = sum(twoDigitNumbers)
print(coordinates)

# data = open('day1.txt', 'r')
# allData = []

# for line in data:
#     allData.append(line.strip())

# def replace_words_with_numbers(text):
#     words_to_numbers = {
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9'
#     }

#     for word, number in words_to_numbers.items():
#         text = text.replace(word, number)

#     return text

# def double_single_digit_numbers(text):
#     for i in range(1, 10):
#         text = text.replace(str(i), str(i) * 2)
#     return text

# def sum_two_digit_numbers(text):
#     numbers = [int(num) for num in text.split() if len(num) == 2 and num != '10']
#     return sum(numbers)

# def process_text(text):
#     text = replace_words_with_numbers(text)
#     text = ''.join(filter(str.isdigit, text))
#     text = double_single_digit_numbers(text)
#     result = sum_two_digit_numbers(text)
#     return result

# text = "Two plus two is four, and five plus six is eleven."
# result = process_text(text)
# print("Sum of two-digit numbers in the text:", result)

# allNumbers = []
# for element in allData:
#     lineNumber = ''.join(char for char in element if char.isdigit())
#     if lineNumber:
#         allNumbers.append(int(lineNumber))

# twoDigitNumbers = []
# for number in allNumbers:
#     if number <= 9:
#         newnumber = number * 10 + number
#     else:
#          firstDigit = int(str(number)[0])
#          secondDigit = int(str(number)[-1])
#          newnumber = firstDigit * 10 + secondDigit
#     twoDigitNumbers.append(newnumber)

# coordinates = sum(twoDigitNumbers)

# print(coordinates)

