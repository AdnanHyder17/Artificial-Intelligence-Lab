# 1)The Fibonacci sequence is a sequence of numbers where the number is the sum of two
# previous numbers. Write the Fibonacci sequence through recursion of 10.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i))





# 2) lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# Given the nested list, extract the word “hello”
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

hello = lst[3][1][2][0]

print(hello)





# 3) d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
# Given the nested dictionary, extract the word hello
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

hello = d['k1'][3]['tricky'][3]['target'][3]

print(hello)





# 4) You are in a hurry and the traffic officer stops you. Write a function
# to return one of 3 possible results: "No fine", "Less Fine", or "Car seize".
# If your speed is 70 or less, the result is "No fine". If speed is between 71
# and 80 inclusive, the result is "Less Fine". If speed is 81 or more, the result is "Car seize".
# Unless it is your anniversary (encoded as a boolean value in the parameters of the
# function) -- on your anniversary, your speed can be 10 higher in all cases
def traffic_fine(speed, is_anniversary):
    # Adjust speed if it's the anniversary
    if is_anniversary:
        speed -= 10
    
    if speed <= 70:
        return "No fine"
    elif 71 <= speed <= 80:
        return "Less Fine"
    else:
        return "Car seize"

speed = int(input("Enter your speed: "))
anniversary_input = input("Is it your anniversary? (yes/no): ").strip().lower()

# Convert anniversary input to boolean
is_anniversary = anniversary_input == 'yes'

print(traffic_fine(speed, is_anniversary))






# 5) Determine whether your data contains any duplicate element in a given array of integers.
# Return true if any value appears twice in the array and return false if every element is
# distinct. Also, remove the duplicates.
def check_and_remove_duplicates(arr):
    # Create a set from the array
    unique_elements = set(arr)
    
    # Check if there were duplicates
    has_duplicates = len(unique_elements) < len(arr)
    
    # Convert the set back to a list
    unique_list = list(unique_elements)
    
    return has_duplicates, unique_list

# Example usage:
arr = [1, 2, 3, 4, 4, 5, 6, 7, 7]
has_duplicates, unique_list = check_and_remove_duplicates(arr)

print("Contains duplicates:", has_duplicates)
print("Unique elements:", unique_list)






# 6) Write a Python program to read a given CSV file as a list.
import csv

def read_csv_as_list(file_path):
    csv_data = []
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data

# File path to the CSV file
file_path = 'Test.csv'

# Read CSV data into a list
csv_data = read_csv_as_list(file_path)

print(csv_data)






# 7) A user enters any string containing letters and digits both. Calculate the number of letters
# and digits entered by a user.
def count_letters_and_digits(input_string):
    letter_count = 0
    digit_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letter_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
    
    return letter_count, digit_count

user_input = input("Enter a string containing both letters and digits: ")

letters, digits = count_letters_and_digits(user_input)

print(f"Number of letters: {letters}")
print(f"Number of digits: {digits}")

