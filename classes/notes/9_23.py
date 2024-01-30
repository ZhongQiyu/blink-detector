# 9/16-9/17

"""
Integers and Rational Numbers:
Algebra:
Geometry:
Function and Images:
Statistics and Probabilities:
3D Geometry:
"""

# 9/16: REVIEW of Data Types

# 1st API:
# - design a function that takes a String input from user, basically an input with a space between two numbers
# - the function performs addition, subtraction, multiplication, and division
# - return the arithmetic result as an array
# - say the user input is "10 20", you want to have [30, -10, 200, 0.5] returned. A: first number; B: second number
# - Example: getArith(5,5)
# - Output: [10, 0, 25, 1.0]

def get_arith(num_str):
  if not isinstance(num_str, str): #Makes sure that the input is not something other than string
    return "Invalid Input"
  else:
    answer = []
    num_list = num_str.strip().split()
    i = 0
    while i < len(num_list):
      if not (num_list[i].isnumeric()): #Make sure one of the items aren't a string
        return "Invalid Input"
      i += 1
    num1 = int(num_list[0])
    num2 = int(num_list[1])
    answer.append(num1 + num2)
    answer.append(num1 - num2)
    answer.append(num1 * num2)
    if num2 == 0:
      answer.append("Error")
      print("Tried to divide by Zero!")
    else:
      answer.append(num1 / num2)
    return answer

# print(get_arith(input("give 2 nums\n")))


# 9/17: 2nd API:
# - extend the 1-dimensional array to be 2-dimensional:
# - design another function that takes an array of data as input, and another one that assists with the arithmetic
# - still, perform four types of operations
# - but we want the array of data that is passed in to make each type of operations based on their index
# - X: first array; Y: second array (Arithmetic one); Z: Number of items in each array
# data = [80, -20, 1500, 0.6]
# api_array = [1, 2, 3, 4]
# want to return [[81, -18, 1503, 4.6],[79, -22, 1497, -3.4],[80,-40,4500,2.4],[80,-10,500,0.15]]

def arith(a,b,op):
  amount = len(a)
  sub_answer = []
  result = 0
  for i in range(amount):
    match op:
      case "+":
        result = int(a[i]) + int(b[i])
      case "-":
        result = int(a[i]) - int(b[i])
      case "*":
        result = int(a[i]) * int(b[i])
      case "/":
        result = "Error" if int(b[i]) == 0 else int(a[i]) / int(b[i])
    sub_answer.append(result)       
  return sub_answer
    
def arrays_arith(numbers, assist_nums):
  answer2 = []                    
  operators = ["+", "-", "*", "/"]
  for i in range(len(operators)):
    answer2.append(arith(numbers,assist_nums, operators[0]))
    operators.remove(operators[0])
  return answer2

# print(arrays_arith([50,50,50,50,50], [1,2,3,4,5]))

#Homework: Make the two functions be able handle any count of numbers in each array, and make arguments for both so easy for API use to use
#xiaoyu991214@gmail.com
#.py
#PyCharm Community Version
#allenzhong

#Hi teacher :)
#Hi there! How can I help



# 9/22-9/23


# 9/22

# mathematically to say rules: formula
# y = a*x + b
# a is the slope, b is the intercept at y axis

import random
# x = [random.randint(1,100) for i in range(100)] # list comprehension
# print(x)

#Homework:

# Task 1:
# - say that we have already have X, as an array of random values between 1 (inclusive) and 100 (exclusive)
# - build a function that takes X and an array of coefficient pairs, inside which:
#   - in each coefficient pair, A stands for the slope and B for the y-axis intercept of a line (basically a formula that looks like the one I provided)
#   - the function iterates through the array, changing x over time
#   - return the x when the final coefficient pair is applied as a transformation formula (y = ax+b)

# func(x,coefs):
# x: [1, 2, 3, 4, 5]
# coefs: [[1, 2],[-1,-2],[3,4],[-5,6],[7,-8],[-9,-10]]
# - in the first pair, a is 1 and b is 2; so x becomes [1,2,3,4,5] and [3,4,5,6,7]
# - in the second, a is -1 and b is -2; so x becomes [-3,-4,-5,-6,-7] and then [-5,-6,-7,-8,-9]
# - etc.
# return the modified x


# 9/23

# import sklearn
# import sklearn.datasets
# data = datasets.iris
# scikit-learn: Machine Learning package for machine learning
# https://scikit-learn.org/

# Task 2: design a function that reuses arrays_arith to extract the extreme values from the result array

def arith(a,b,op):
  amount = len(a)
  sub_answer = []
  result = 0
  for i in range(amount):
    match op:
      case "+":
        result = int(a[i]) + int(b[i])
      case "-":
        result = int(a[i]) - int(b[i])
      case "*":
        result = int(a[i]) * int(b[i])
      case "/":
        result = "Error" if int(b[i]) == 0 else int(a[i]) / int(b[i])
    sub_answer.append(result)       
  return sub_answer
    
def arrays_arith(a, b):
  answers = []
  operators = ["+", "-", "*", "/"]
  for i in range(len(operators)):
    answers.append(arith(a,b,operators[0]))
    operators.remove(operators[0])
  return answers

def extreme_extract(list):
  new_arr = list.copy()
  for i in range(len(new_arr)):
    if isinstance(list[i], str):
      new_arr.pop(i)
  new_arr.sort()
  min = new_arr[0]
  max = new_arr[len(new_arr) - 1] 
  return max, min

def main():
  a = input("Please input a: ").split(" ")
  b = input("Please input b: ").split(" ")
  extremes = []
  answers = arrays_arith(a,b)
  for answer in answers:
    extremes.append(extreme_extract(answer))
  return extremes

#print(main())

#When we dont do .copy, we are setting theoriginal array to two names, so when we do something to amo or bmo its doing it to the same array
#When we do .copy, we get two arrays, so doing sometihing to one doesnt affect the other



# 9/29-9/30


# 9/29

# Task 1:
# - say that we have already have X, as an array of random values between 1 (inclusive) and 100 (exclusive)
# - build a function that takes X and an array of coefficient pairs, inside which:
# - in each coefficient pair, A stands for the slope and B for the y-axis intercept of a line (basically a formula that looks like the one I provided)
#   - the function iterates through the array, changing x over time
#   - return the x when the final coefficient pair is applied as a transformation formula (y = ax+b)

# coefficient pair: (a,b)

# func(x,coefs):
# x: [1, 2, 3, 4, 5]
# coefs: [[1, 2],[-1,-2],[3,4],[-5,6],[7,-8],[-9,-10]]
# - in the first pair of coefs, a is 1 and b is 2; so x becomes [1,2,3,4,5] and [3,4,5,6,7]
# - in the second, a is -1 and b is -2; so x becomes [-3,-4,-5,-6,-7] and then [-5,-6,-7,-8,-9]
# - etc.
# return the modified x

# when y = a*x + b
# y can also be known as f(x)
# say x = 1, then f(x) = f(1), giving us f(1) = a + b

def formula(a,b,x):
  return (a*x) + b

def main2():
  x = [1,2,3,4,5]
  coefficients = [[2,3],[3,4],[4,5],[5,6],[6,7]]
  #print(formula(coefficients[0][0], coefficients[0][1] , x[0])) -- Outputs 5 (sample for me to look at)
  for coef in coefficients:
    x = [formula(coef[0],coef[1],xv) for xv in x] # list comprehension
    print(x)
  y = x # just to make the output more readable
  return y

#print(main2())

# int, float, double, booleans: data types -- data structures

"""
Homework:

Task 1:
- Something called as dictionary in Python exists.
- Read through the examples provided in https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- And construct a dictionary of a card suite that contains 4 types of card colors and 13 types of card values. (either through a plain function call or a helper function)

*Task 2:
- Set up an array of arrays:
  - each inner array inside the outer array would be a coordinate of a city in California
  - the outer array is the data storage of a small 2D map, which makes sense because the outer array contains all the coordinates of cities in California
- Design a function that takes two String inputs, one is for city A, the other for city B, computing the distance between the two cities (preserving 4 decimal points)
- *Use dictionary and perform the same task.
"""

"""
Pre-Calculus: first derivative
Image: High Dimensional Data; Arrays Concatenated
Coding Systems: binary, octal, decimal, hexadecimal
"""

cardDictionary = {}

def switch(card):
  letter_card = ""
  match card:
    case 12:
      letter_card = "K" # King
    case 11:
      letter_card = "Q" # Queen
    case 10:
      letter_card = "J" # Jack
  return letter_card

def type_of_card(type):
  card_type = ""
  match type:
    case 0:
      card_type = "S" # Spades
    case 1:
      card_type = "H" # Hearts
    case 2:
      card_type = "C" # Clubs
    case 3:
      card_type = "D" # Diamonds
  return card_type

def whole_set():
  cards = []
  for i in range(13):
    if i == 0:
      cards.append("A") # Ace
    elif i >= 1 and i <= 9:
      cards.append(i)   #Numbers 1-10
    elif i>= 10 and i <= 13:
      cards.append(switch(i)) # Jack, Queen and King
  return cards

def card_dict():
  for i in range(4):
    cardDictionary[type_of_card(i)] = whole_set()
  return cardDictionary

#print(card_dict())

# A set of cards w/o jokers
# card types: spade, heart, club, diamond
# card values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K


# 9/30

import math

map = {
  "KFC": [12,10],
  "Mcdonalds" : [12,26],
  "Wendy's" : [1912,102012901],
  "Walmart" : [0,0]
      }

def calculate_distance(first, second):
  X1 = int(map[first][0])
  Y1 = int(map[first][1])
  X2 = int(map[second][0])
  Y2 = int(map[second][1])
  result = math.sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1))
  return result

# print(calculate_distance("Mcdonalds", "Wendy's"))
# print(round(16000,4))
# y=ax+b
