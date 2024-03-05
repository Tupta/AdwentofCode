##test


# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

data = {'1abc3', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'}

newdata = set()
for item in data:
    numbers = ''.join(char for char in item if char.isdigit())
    newdata.add(numbers)

print(newdata)

first_last_digits = set()
for item in newdata:
    first_last = item[0] + item[-1]
    # if len(item) == 1:
    #     first_last = item * 2
    first_last_digits.add(first_last)

print(first_last_digits)