# 10/6

"""
Task: Put Them All Together - Calculate The Similarity of Two Triangles

- Q1: How many parameters are there in a triangle? How many do we need to certify a triangle?
  - A: 3 sides, 3 verticies, 3 angles that add up to 180.
  - To certify a shape is a triangle, the angles have to add up to 180, it has to be a concave polygon, it has to have exactly 3 sides, it has to have 3 segment sides that aren't bent, also has to be a closed shape. 

- Q2: Is there a way to find an angle of a triangle with its lengths?
  - A: If it is a equilateral triangle, each angle is 60.
  - A: If it's a right triangle, use sine cosine and tangent. If it is another type of triangle, you cant calculate the angles just by the sides.

- Q3: Design a program that takes two sets of parameters for triangles, respectively

  - Q3.1: Inside the first function, determine the types of each parameter, and put them as a list. Sides are integers, and angles are float values. Assume that the sets of parameters have the same counts for each type of parameter. For example:
    - Input: [(3, 4, (5, 6), arctan(3/4)), (6, 9, (12, 15), arctan(3/2))]
    - Output: ['side','side','vertice','angle']

  - Q3.2: Inside the second function, determine if we can compare the two triangles or not. By means of 'comparable', we need to have the same count of each type of parameters. For instance, [(1, (2,3), arcsin(1/2)),(4, (5,6), arcsin(1/3))] gives us a comparable pair, but [(1, (2,3), arcsin(1/2)),(4, (5,6), (7,8), arctan(sqrt(2)))] does not.
    - Hint: Are they having sufficient counts of parameters? If does, what could be a simple way to compare? If doesn't, what do we need to add as parameters?

  - Q3.3: Inside the third function, use the parameters generated from the list of integers, compute the 'degree of similarity' between two triangles. We would use the following rules for the sake of parsing:
    - If the two triangles are not comparable, return -1;
    - Otherwise:
      - 1 amount of side's difference will bring 1 'degree's difference e.g. if triangle A has a length 3 side and B has one of length 4, then add 1 'degree' to the total, since |3-4|*1=1
      - 1 amount of each coordinate's dimension will bring 0.1 'degree's difference e.g. if triangle A has a vertice at (1,3) and B has one at (2,4), then add 0.2 'degree's to the total, since (|1-2|+|3-4|)*0.1=0.2
      - 1 amount of an angle's difference would bring 0.01 'degree's difference e.g. if triangle A has an angle of degree 75 and B has one of degree 70, then add 0.05 'degree's to the total, since |75-70|*0.01=0.05
    - Input: [(1, (2,3), (4,5), arcsin(sqrt(2)/4)), (5, (6,7), (8,9), arcsin(2*sqrt(2)/5))]
    - Output: |1-5|*1+(|2-6|+|3-7|+|4-8|+|5-9|)*0.1+|arcsin(sqrt(2)/4)-arcsin(2*sqrt(2)/5)|*0.01=5.602399...

coef_sd = 1
coef_cd = 0.1
coef_ad = 0.01
similarity = s_sd*coef_sd + s_cd*coef_cd + s_ad*coef_ad

  - *Q3.4: How can I vary the coefficients of 'degree's to make the difference between the digit

VERSION REVISED
"""

# 10/6

def trig_param_types(params):
  types = []
  for i in params:
    if isinstance(i, tuple): 
      types.append("Vertice") # find out what is what from given list, and return strings
    elif isinstance(i, float):   
      types.append("Angle")
    else:
      types.append("Side")
  return types

def param_types(all_params):
  all_types= []
  all_types.append(trig_param_types(all_params[0]))
  all_types.append(trig_param_types(all_params[1])) 
  return all_types

# print(triangle_values([[(6,3),8,9,0.31],
                        #[8,(28,8),9,0.9291]]))

# ------------------------------------

def trig_param_stats(array):
  dict = { 
    'Sides': 0,
    'Vertices': 0,
    'Angles' : 0
  }
  for i in array:                           #Goofy ahh thingy
    if i == "Side":
      dict["Sides"] += 1
    elif i == "Vertice":
      dict["Vertices"] += 1
    elif i == "Angle":
      dict["Angles"] += 1
  return dict

def comparing_triangles(array):  #This function is used for comparing two triangles in sub arrays in one given array
  trig1_types = trig_param_types(array[0])
  trig2_types = trig_param_types(array[1])
  trig1_stats = trig_param_stats(trig1_types) 
  trig2_stats = trig_param_stats(trig2_types)
  if trig1_stats == trig2_stats:
    return "Comparable!"
  return "Not Comparable!"              #Return Values

# print(comparing_triangles([[(6,3),8,9,0.31],[8,(28,8),9, 0.20909209120,2829819210.21231]]))

# ------------------------------------

def type_similarity(a,b,val_type): # math function to compute degree of similatiry (helper)
  # modular: leave the smallest, meaningful chunks of computation to the helpers (i.e. the parameters that a helper function takes should be as simple as possible)
  if val_type == "Sides": # x, y, ... (integers)
    return abs(a-b)*1
  elif val_type == "Vertices": # (x, y) (tuple of integers)
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))*0.1
  elif val_type == "Angles": # x, y, ... (floats)
    return abs(a-b)*0.01
  else:
    return "Invalid Input!"

def trig_param_data(trig_data):
  params = {
    'Angles': [],
    'Vertices': [],
    "Sides" : []
  }
  for i in range(len(trig_data)):
    value = trig_data[i]
    if isinstance(value, tuple):
      params["Vertices"].append(value)
    elif isinstance(value, float):
      params["Angles"].append(value)
    else:
      params["Sides"].append(value)
  return params

def degree_of_sim(array):
  trig1 = array[0]
  trig2 = array[1]
  trig1_params = trig_param_data(trig1)
  trig2_params = trig_param_data(trig2)

  degree = []
  
  for type, values in trig1_params.items(): # key-value loop
    trig1_vals = values
    trig2_vals = trig2_params[type]
    for i in range(len(trig1_vals)):
      degree.append(type_similarity(trig1_vals[i],trig2_vals[i], type))
  
  return sum(degree)
  
test_array = [[8, 7,(6,9), 0.282319], [8, 7,(6,23923), 0.28123219]]
#print(degree_of_sim(test_array))

# Instructor's Reflections:
# - Change the questions and examples in the class more interesting so that they relate with games, etc. but keep the seriousness when it is needed
# - Try to add some statistics
# - Find a way to run another file other than just main.py (x
# - Follow up with personal timelines in studies and workload

# 10/7

"""
Homework: DESIGN

- Q1: Usage of Parameters

  - Q1.1: If we only know about the sides of a triangle, how many parameters do we need to certify it? What if only vertices? What if only angles?
  -A: Please say what "it" stands for. 
  
  - Q1.2: If we know about two types of parameters in a triangle, what is the minimum count of parameters to certify it?
  - A: To certify What? What is "it"?
  
  - Q1.3: If we know about all three types of parameters in a triangle, plus that we do not have complete information (i.e. no 3 counts of sides/vertices/angles) about any type, what is the minimum count of parameters to certify it?
  - A: We will need 5 to certify that it is a triangle. 

- Q2: Review of triangular functions

  - Q2.1: sin(x) and cos(x)
    - sin(pi/2) = cos(?) = 0
    - sin(pi/4) = cos(?) = pi/4
    - sin(pi/6) = cos(?) = 1/3 Pi
    - sin(pi/8) = cos(?) = 3/8 Pi
    
  - Q2.2: tan(x) and cot(x)
    -tan(pi/2) = cot(?) = i don't know what cot is...
    - tan(pi/4) = cot(?) = 
    - tan(pi/6) = cot(?) = 
    - tan(pi/8) = cot(?) = 
    
  - Q2.3: The Inverse (arc-sin/cos/tan/cot)
    - What is the domain of arcsin(x)? What about arccos(x)?
    - I haven't learned this concept yet
    - What is the domain of arctan(x)? What about arccot(x)?
    -I haven't learned this concept yet
    
  - Q2.4: Can we always write an angle in a triangle in the form of The Inverse? Why?
  - A: Yes because the inverse sine or cos of something is still a number. 

- Q3: Program Design - Calculate The Similarity of Two Triangles

  - Q3.0: How many ways do we have to determine if two triangles are similar, mathematically?
  - A: Angles and sides, so 2 ways.

  - Q3.1: Design a function that takes a dictionary of parameters for a triangle, and return the list that contains the types for each parameter. Sides are integers, and angles are float values. Assume that all inputs make sense (i.e. they form legit triangles). For examples:
    - I1: {"AB":1, "BC":sqrt(2), "CA":sqrt(3)]
    - O1: ['side','side','side']
    - I2: {"AB":6, "A":(2, 3), "BC":3*sqrt(2), "C":(5, 6), "ABC":45]
    - O2: ['side','vertice','side','vertice','angle']


"""
def determine_triangles(dict):
  types = []
  
  for key, values in dict.items():
    if len(key) == 1:
      types.append("Vertice")
    elif len(key) == 2:
      types.append("Side")
    elif len(key) == 3:
      types.append("Angle")
    else:
      return "Invalid Arguments!"
  return types

#print(determine_triangles({"A": "(5,6)" , "cab" : 45, "BC" : 5}))
"""

  - Q3.2: Design a function to determine if we can compare the two triangles or not. By means of 'comparable', we mean to have two certified triangles. When the triangles are comparable, we approach True, False otherwise. The parameter for this function will be a list of dictionaries, for instance:
    - I1: [{"AB":1, "A":(2,3), "BAC":arcsin(sqrt(3)/2), "C":(2+sqrt(2),3+sqrt(2))},{"DE":4, "D":(5,6), "EDF":arccos(1/3), "F":(7,6+2*sqrt(2))}]
    - O1: True
    - I2: [{"AB":1, "A":(2,3), "BAC":arcsin(sqrt(3)/2)},{"DE":4, "D":(5,6), "EF":12, "EDF":arccos(1/3)}]
    - O2: False
    - I3: [{A":(2,3), "B":(3,4), "C":(4,3)},{"DE":5, "EF":5*sqrt(3), "DF":10}]
    - O3: False (Why?)
    - I4: [{A":(2,3), "B":(3,4), "C":(4,3)},{"DE":5, "D":(0,1), "EF":5*sqrt(3), "F":(10,1), "DF":10}]
    - O4: True (Why?)
    - Hint1: Do you think the list we obtained from the first function to be useful?
    - Hint2: How to ensure that we have two certified triangles?

"""
#I use the helper from the last one to do this one



def comparability_of_triangles(list):
  if len(list) > 2: 
    return "Invalid List!"
  trig1 = list[0]
  trig2 = list[1]
  result1 = determine_triangles(trig1)
  result2 = determine_triangles(trig2)
  total_verticies1 = 0
  total_angles1 = 0
  total_sides1 = 0

  total_verticies2 = 0
  total_angles2 = 0
  total_sides2 = 0
  
  for i in result1:
    if i == "Vertice":
      total_verticies1 += 1
    elif i == "Side":
      total_sides1 += 1
    elif i == "Angle":
      total_angles1 += 1
  for i in result2:
    if i == "Vertice":
      total_verticies2 += 1
    elif i == "Side":
      total_sides2 += 1
    elif i == "Angle":
      total_angles2 += 1
      
  if total_verticies1 == total_verticies2 and total_sides1 == total_sides2 and total_angles1 == total_angles2:
    return True
  else:
    return False

#print(comparability_of_triangles([{"A": "(5,6)" , "cab" : 45, "BC" : 5}, {"A": "(5,6)" , "de" : 45, "BC" : 5}]))






"""

  - Q3.3: 
    - Design a function that compute the 'degree of similarity' between two comparable triangles. The input is assumed to be comparable, and the amount of similarities is based ONLY on the given, ORDERED array of parameters.
    - We would use the following rules for parsing:
      - 1 amount of side's difference will bring 1 'degree's difference e.g. if triangle A has a length 3 side and B has one of length 4, then add 1 'degree' to the total, since |3-4|*1=1
      - 1 amount of each coordinate's dimension will bring 0.1 'degree's difference e.g. if triangle A has a vertice at (1,2) and B has one at (2,3), then add 0.2 'degree's to the total, since (|1-2|+|2-3|)*0.1=0.2
      - 1 amount of an angle's difference would bring 0.01 'degree's difference e.g. if triangle A has an angle of degree 75 and B has one of degree 70, then add 0.05 'degree's to the total, since |75-70|*0.01=0.05
      - i.e. similarity = sd*coef_sd + cd*coef_cd + ad*coef_ad
    - I1: [{"AB":2, "A":(2,3), "C":(4,5), "BAC":arcsin(sqrt(2)/2)}, {"DE":6, "D":(6,7), "E":(8,7+4*sqrt(2)), "EFD":arcsin(1/2)}]
    - O1:
      - sd: |2-6|*1
      - cd: (|2-6|+|3-7|+|4-8|+|5-(7+4*sqrt(2))|)*0.1
      - ad: |arcsin(sqrt(2)/2)-arcsin(1/2)|*0.01
      - similarity ~= 6.039
    - Hint: recall the turtle library in Python to help visualization, if needed.













    

  - *Q3.4: How can we refactor the function obtained from Q3.3 so that we compute similarities based on all parameters of the two comparable triangles?


  
"""

# 10/8 HW

"""
Homework:

Delaunay's Triangle - Detect the Features of a Face

Q1:
- Q1.1: In general, how would we look at a map that has data across a certain range of area?
  - For example, if you are in front of the building where Coding Minds locates, and you would want to go to the City Hall in Irvine, how would you scroll up and down with your screen so that the inspection of a zone would make up for your determination?
- Q1.2: In the meantime, when we want to project the area of a city down to somewhere where you need additional scrolling up and down for getting to know the, from 3D to 2D, what kind of information do we lose?
  - Think about the time when we are watching the building blocks from different angles. Do we lose some information when we inspect the Oriental Pearl TV Tower from the ground?
- Q1.3: Would you think it to be meaningful to compensate for the loss of information when we look upon the objects? Why?

Q2:
- Q2.1: explore the library turtle in Python.
  - How would you transfer your project experience from Lua/Roblox, especially in terms of computer graphics/gaming interface, to the program in Python?
  - There would be operations and operators that involve geometric transformation. In this case, should we allow the visualization to work upon the original set of points. We can invoke the turtle library so that they can become the information that can help the locking process for the image's features.
- Q2.2: Design a function that takes three parameters, a, b, and c, representing the lengths of three sides lying within the triangle. Would there be a situation that overcomes the constraint happened upon the parameter of only-lengths? We would allow the situation to happen across the given set of images.
- Q2.3: Design a function that overcomes the limitation of parameters in order to gain the feature importance, by exactly plotting the triangle out so that it achieves the identity of different .

"""

# 0. Model and Predictions

# 1. Pipeline of Detection: What steps do we need for parsing the image so that it would be ready for detection?
#   - How do we know that the data, first of all, is of format similar to an image?
#   - Once we know that an image makes sense, what do we do to let the transformation happen? Or, is there even a way to comply with the do we even need transformation? Why?
#   - When we have the image prepared, would we allow the permission to happen upon the predictive model?
#   - Is there a way to parse the function so that it permits the data to be updated and used for prediction efficiently? If yes, then how? If no, then why?
#   - In which way can we notice the patterns where the updated functionalities can make complete sense?
#   - Would that be sufficient to let the final result be persuative to the viewers?

# 2. Tech Stacks: What tools do we use to realize the functions?
#   - If we know event-oriented programming already in web technologies, then do we have an option to find equivalences in Python (JavaScript to Python)? Why and how we can apply them?
#   - If we already know that Lua and Roblox fit the scenes of UI-intensive programming, especially building up applicatoins, then do you think that we have similar tools for handling in Python?
#   - How often we would be able to maintain the effectiveness for joining all the sub-processes? In general, each pipeline plays as a part, but there would be situations where hardware-related issues come up to our mind, telling the stories or giving clues towards where we are over the days. If there would be a chance to notice the the traces that happen through the hardware, letting us to know the attitu attributes that are available so that the overall stance would be as helpful as the other does. In general, we would take the situation seriously, so that the pipeline would make further reusability towards the facts instead.
#   - Is there a way where we can apply the tools across the the existent modules?
#   - Take the consideration to be serious, we would be notified to pull the data along the existent 



import math
import time

from turtle import *

# 10/13-10/14

# Task 0: Object-Oriented Programming

# a class, in terms of programming, is an abstraction of real-world objects
# abstraction is a model that simulates the behaviors of objects (it might a bit abstract)

# character (a class: it is a type of object; it has a bunch of different behaviors)
# - create blocks
# - make interactions with NPC
# - talk /..

# We invoke Turtle as a way to perform the simulation of
# tasks that might be involving a 2-D (or even 3-D) planes

"""
t = Turtle() # call the constructor of class Turtle, to make the Turtle object



# Task 1: Triangles

increment = 200

def triangle():
    # (30, 60, 90) triangle
    t.forward(1 * increment)
    pos1 = t.pos()
    t.left(120)
    t.forward(2 * increment)
    t.left(150)
    t.forward(347)
    # preserve the positions of the first triangle

    # (45, 45, 90) triangle
    t.forward(1 * increment)
    t.left(135)
    t.forward(1.41421356237 * increment)
    t.left(135) # dynamic
    t.forward(1 * increment) # dynamic
    pos2 = t.pos()
    # preserve the positions of the second triangle

# Challenge:
# Compute the distance between the first point in the 30-60-90
# triangle and the last point in the 45-45-90 triangle.
# result = math.sqrt(math.pow(pos1[1] - pos2[1], 2) + math.pow((pos1[0] - pos2[0]), 2)) 
# print(result)



# Task 2: Rectangles, Squares, Circles, and Trapezoids

# Challenge: Draw a rectangle with a side of increment, the other being 2*increment.
# t.left(angle) # or t.right(angle)
# t.forward(1 * increment)
# t.left(angle)
# t.forward(1*increment)
# t.left(angle)
# t.forward(1*increment)
# t.left(angle)
# t.forward(1*increment) 

def rect(x,y,width,height):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

def triangle(x1,y1,x2,y2,x3,y3):
    t.setpos(x1,y1)
    t.setpos(x2,y2)
    t.setpos(x3,y3)
    t.setpos(x1,x1)
    # next time, involve angles instead of setpos()

def square(x,y,s):
    t.penup()
    t.home()
    t.right(90)
    t.setpos(x,y)
    t.pendown()
    for i in range(4):
        t.forward(s)
        t.left(90)
    t.left(90)

def circle(x,y,r): # be aware of naming* it needs to be CONCISE
    t.penup()
    t.home()
    t.setpos(x,y)
    t.pendown()
    t.circle(r)

def trapezoid(x,y,x2,y2,a,b):
    t.penup()
    t.home()
    t.setpos(x,y)
    t.pendown()
    t.forward(a)
    t.setpos(x2 + b,y2 + b)
    t.left(180)
    t.forward(b)
    t.setpos(x, y)
    t.left(180)

trapezoid(200,200,100,100,50,200)
"""

# 10/13 HW: design functions that compute the center of a 2-D:
# (1) rectangle (square)
# (2) circle
# (3) triangle
# (4) trapezoid

def rect_center(x,y,w,h):
    x_axis = (x + (x + w)) / 2
    y_axis = (y + (y + h)) / 2
    return (x_axis, y_axis)

def circle_center(x,y,r,angle): # basic case
    c1 = math.cos(angle) * r - x
    c2 = math.sin(angle) * r - y
    return (c1, c2)

def triangle_center(x1,y1,x2,y2,x3,y3):
    return ((x1 + x2 + x3)/3, (y1 + y2 + y3)/3)

def trapezoid_center(a,b,h): # assume that the trapezoid is of equal sides
    return (((b + 2 * a) / 3 * (a + b)), (h(b + 2 * a) / 3 * (b + a)))

# Challenge: 
# Pass the functions with matching parameters and show them in the Turtle canvas
# DONE BUT COPY YOUR CODE HERE

# 10/14 HW



# 10/21-10/22 (imported from 10/14)

# HW0:
# - Draw for each function one of the matching shape (e.g. draw a rectangle for rect_center, a circle for circle_center, etc.)
#   - Draw the matching shape by giving the parameters needed (coordinates, side's length, etc.)
#   - Draw the center of these shapes

# - Do a (visually) clockwise traversal for the shape's vertices including their center, using Python turtle
#   - It is known that for some of the functions we don't have complete data for the coordinates, so we need to compute them.
#   - How? Can we modify our current functions and pass them using our new function parameters? (Hint: what do we need for getting ALL of the coordinates?)
#   - Turtle provides styles of lines and arrows. Try to use just one style of line and arrow in each count of movement
#       - e.g. from A to B in a triangle, the line can be blue and the arrow is default; from B to C, the line switches to be red with a round arrow.
#       - This will help us to know the trace for each shape.
#   - At the end of traversal for each shape, we know that the end point sets to be the center.
#       - Keep the data of all the centers.
#       - When all the traversals of shapes are done, do a traversal for the centers too. Keep the trace of this traversal too, with varied styles if needed.

# - Observe all the traces. Include all routines in a function (*bonus: using Object-Oriented Programming) and invoke the function a few times.
#   - Vary the parameters for each run use random-number-generation. Do you find anything that is interesting?
#   - This will be a visual demo for how a MACHINE LEARNING ALGORITHM will learn the features of a FACE.

# HW1:
# - Read the Introduction of OpenCV library in Python (or C++) up to Image Resizing with OpenCV: https://learnopencv.com/getting-started-with-opencv/
#   - Leave comments for the parts where you do not understand.
#   - Compare the ideas of the basic 'processing' routines we have covered so far. How can the images be decomposed into meaningful units? 



# 10/28-10/29

# Project Tech Stacks (1/3)

# The #1 in 1/3 - User Interface：PyQt, Tkinter
# - Use tools like Tkinter to create basic interface, such as buttons and scrolling bars
# - Explain how does the toolsets interact between the back-end and the front-end

# HW0: Read the following code and try to figure out how each line functions

import os
import cv2
import requests
import numpy as np
from pynput import mouse
import matplotlib.pyplot as plt

"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=1)

window = tk.Tk()
window.title("URL Fetcher")
btn = tk.Button(window, text="Plot", command=plot_graph)
btn.grid(row=0, column=0)
window.mainloop()

url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=20)

fetch_button = tk.Button(window, text="Fetch URL", command=fetch_url)
fetch_button.pack()

response_content = tk.StringVar()
response_label = tk.Label(window, textvariable=response_content, wraplength=400)
response_label.pack(pady=20)

window.mainloop()
"""

def fetch_url():
    url = url_entry.get()
    try:
        response = requests.get(url)
        response_content.set(response.text)
    except requests.RequestException as e:
        response_content.set(str(e))
