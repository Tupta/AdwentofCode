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
    
#print(allData) 

allNumbers = []
for element in allData:
   # print(element.strip())
    for char in element:
        lineNumber = ''.join(char for char in element if char.isdigit())
        if lineNumber:
            allNumbers.append(int(lineNumber))

print("linia kontrolna terefere")

newNumberList = []
for number in allNumbers:
    if number <= 9:
        newNumber = int(str(number) * 2)  # Podwojenie jednocyfrowej liczby poprzez jej duplikację
    else:
        first_digit = int(str(number)[0])
        second_digit = int(str(number)[-1])
        newNumber = first_digit * 10 + second_digit
    newNumberList.append(newNumber)

print(newNumberList)

Calibration = sum(newNumberList)
print(Calibration)


# data = open("C:\\Users\\Tupta\\Desktop\\AdwentofCode\\day1\\day1.txt", "r")

# allData = []

# for line in data:
#     allData.append(line.strip())
    
# allNumbers = []
# for element in allData:
#     number_str = ''.join(char for char in element if char.isdigit())
#     if number_str:
#         allNumbers.append(int(number_str))

# print(allNumbers)