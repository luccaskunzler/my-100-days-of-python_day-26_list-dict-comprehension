# first exercise - create a list of square numbers in a single line (list comprehension)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print("\nSquared numbers from a given list")
print(squared_numbers)

# list filtering for even numbers in a single line (list comprehension)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print("\nNumber in a given list that are even")
print(result)

# create a list called result which contains the numbers that are common in both files.
# file1.txt contained: 1, 2, 3
# file2.txt contained: 2, 3, 4
# result = [2, 3]
with open("file1.txt", "r") as file1:
    data1 = (file1.readlines())

with open("file2.txt", "r") as file2:
    data2 = (file2.readlines())

result = [int(num) for num in data1 if num in data2]
print("\nNumbers in both files: ")
print(result)

# dictionary comprehension
import random
names = ['Tony', 'Peter', 'Steve', 'Bruce', 'Thor', 'Clinton', 'Wanda', 'Natasha', 'Stephen']

current_power = {avenger:random.randint(1,100) for avenger in names}
print("\nAvengers Power Level")
print(current_power)

powerful_avengers = {avenger: power for (avenger, power) in current_power.items() if power > 70}
print("\nSuper Powerful Avengers")
print(powerful_avengers)

# exercise 2 with dic comprehension - length of words
michael = "That's what she said"
michael_dict = {word: len(word) for word in michael.split()}
print("\nNumber of characters in every word of famous Michael Scott catch phrase")
print(michael_dict)


# exercise 3 with dic comprehension - repetition of words
pam_speech = '''I didn't watch the whole documentary. After a few episodes, it was too painful. 
I kept wanting to scream at Pam. It took me so long to do so many important things. 
It's just hard to accept that I spent so many years being less happy than I could have been. 
Jim was 5 feet from my desk and it took me four years to get to him. 
It'd be great if people saw this documentary and learned from my mistakes. 
Not that I'm a tragic person. I'm really happy now. 
But it would just just make my heart soar if someone out there saw this 
and she said to herself be strong, trust yourself, love yourself. 
Conquer your fears. Just go after what you want and act fast, because life just isn't that long.'''

# list_pam_speech = pam_speech.split()
# pam_dict = {word: list_pam_speech.count(word) for word in list_pam_speech}
pam_dict = {word: pam_speech.split().count(word) for word in pam_speech.split()}
print("\nNumber of repetitive words in Pam's last speech")
print(pam_dict)

# exercise 4
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: temp_c*9/5 + 32 for (day, temp_c) in weather_c.items()}
print("\nWeather converted to Fahrenheit")
print(weather_f)


# NATO challenge
import pandas
name = input("\nType you name: ").replace(" ", "").lower()
nato = pandas.read_csv("nato.csv")

print("\nMethod 1 - Creation of the list directly")
result_method1 = [nato[nato.letter == character].code.values[0] for character in name]
print(result_method1)

print("\nMethod 2 - with the creation of the dictionary first using iterrows")
nato_dict = {series.letter: series.code for (index, series) in nato.iterrows()}
# nato_dict = {series[0]:series[1] for (index, series) in nato.iterrows()}
result_method2 = [nato_dict[character] for character in name]
print(result_method2)