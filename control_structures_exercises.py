#!/usr/bin/env python
# coding: utf-8

# # Conditional Basics

# ### **A)** 
# Prompt the user for a day of the week, print out whether the day is Monday or not

# In[1]:


is_day = input("Day of the week? - ")
if is_day.lower() == "monday":
    print('It is Monday!')
else:
    print('It is not Monday \n')


# ### **B)** 
# Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 

# In[2]:


is_day = input("Day of the week (type out the full name)? - ")
if is_day.lower() == 'saturday' or is_day.lower() == 'sunday':
    print('Choosen day is part of the weekned \n')
else:
    print("Choosen day is not part of the weekend \n")


# In[3]:


# make a list of the days of the week
days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

#create a a user input for day look up
is_day = input("Day of the week (type out the full day name)? - ").lower()

#create if in function to check if the user input is in days_of_week
if is_day in days_of_week:
    #if return true then check if the day is a weekend or week day
    if is_day == 'saturday' or is_day == 'sunday':
        print('Choosen day is part of the weekend \n') 
    else: 
        print ("Choosen day is not part of the weekend \n")
# if user input is not a day of the week
else:
    print("You didn't pick a day of the week \n")


# ### C)
# Create variables and make up values for:
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# 
# Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[4]:


# generate random integer values
from random import seed
from random import randint
# seed random number generator
# generate some integers

for N in range(1):
    Hours = randint(30, 70)
    print(f"You worked {Hours} hours.")

for n in range(1):
    Rate = randint(26, 48)
    print(f"You were paid {Rate} an hour.")


if Hours <= 40:
    Pay = Rate * Hours
    print("You worked 0 overtime hours")
    print(f"You'll be paid {Pay} for the week \n")
elif Hours > 40:
    OTPay = Rate * 40 + (Rate * 1.5 * (Hours - 40))
    print(f"You worked {Hours - 40} hours of overtime ")
    print(f"You'll be paid {OTPay} for the week \n")


# # Loop Basics

# ### While
# 
# * Create an integer variable i with a value of 5.
# * Create a while loop that runs so long as i is less than or equal to 15
# * Each loop iteration, output the current value of i, then increment i by one.

# In[5]:


i = 5
while i <= 15:
    print(i)
    i += 1
print("")

# * Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# 

# In[6]:


i = 0 
while i <= 100:
    print(i)
    i += 2
print("")

# * Alter your loop to count backwards by 5's from 100 to -10.

# In[7]:


i = 100
while i >= -10:
    print(i)
    i -= 5
print("")

# * Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

# In[8]:


i = 2
while i < 1_000_000:
    print(i)
    i *= i
print("")

# * Write a loop that uses print to create the following output:
# <br>100
# <br>95
# <br>90
# <br>85
# <br>80
# <br>75
# <br>70
# <br>65
# <br>60
# <br>55
# <br>50
# <br>45
# <br>40
# <br>35
# <br>30
# <br>25
# <br>20
# <br>15
# <br>10
# <br>5

# In[9]:
i = 100
while i >= 5:
    print(i)
    i -=5
print("")

# ### For Loops
# 

# * Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[10]:


is_number = int(input("Pick a number - "))
for n in range(1, 11):
    print(f"{is_number} x {n} = {is_number * n}")
print("")   


# * Create a for loop that uses print to create the output shown below.

# In[11]:

for n in range(1, 10):
    print(str(n) * n)   
print("")

# ### break and continue

# * Prompt the user for an odd number between 1 and 50. 
# * Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# * Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[12]:


while True:
    picked_odd = input("Pick and odd number from 1 - 50 - ")
    if picked_odd.isdigit() and int(picked_odd) % 2 != 0 and int(picked_odd) in range(1,51):
        break
print(f"Number to skip is {picked_odd} \n")

picked_odd = int(picked_odd)
for n in range(50):
    if n % 2 == 0:
        continue
        
    if n == picked_odd: 
        print(f"Yikes! Skipping number: {n}")
        continue
        
    print(f'Here is an odd number: {n}')
print("")

# * Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

# In[13]:

while True:
    picked_number = input("Count from 0 to ")
    if picked_number.isdigit() and int(picked_number) > 0:
        break 
print("")
picked_number = int(picked_number)

for n in range (picked_number + 1):
    print(n)
    n =+ 1
print("")

# In[14]:


while True:
    picked_number = input("Count to 1 from ")
    if picked_number.isdigit() and int(picked_number) > 0:
        break
print("")
picked_number = int(picked_number)

while picked_number >= 1:
    print(picked_number)
    picked_number -= 1

print("")
# # Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
# * Write a program that prints the numbers from 1 to 100.
# * For multiples of three print "Fizz" instead of the number
# * For the multiples of five print "Buzz".
# * For numbers which are multiples of both three and five print "FizzBuzz".

# In[15]:


for n in range (1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        continue
    if n % 3 == 0:
        print ("Fizz")
        continue
    if n % 5 == 0:
        print("Buzz")
    print(n)
    n += 1
print("")

# ### Display a table of powers.
# 
# * Prompt the user to enter an integer.
# * Display a table of squares and cubes from 1 to the value entered.
# * Ask if the user wants to continue.
# * Assume that the user will enter valid data.
# * Only continue if the user agrees to.

# In[16]:


# If we want the user to continue after each iteration
while True: 
    picked_number = input("Pick a number - ")
    if picked_number.isdigit() and int(picked_number):
        break
    print("")
    
picked_number = int(picked_number)
for n in range (1, picked_number + 1):
    powers = [n] + [n*n] + [n*n*n]
    print(powers)
    if input("Would you like to continue (y/n) - ").lower() != 'y':
        break
print("")

# In[17]:


# If we want the users to be able to enter another number after the first
number = []
squared = []
cubed = []
names = ['number', 'squared', 'cubed']

while True:
    while True:
        picked_number = input("What number would you like to go up to? - ")
        if picked_number.isdigit():
            picked_number = int(picked_number)
            break
        
    for n in range (1, picked_number + 1):
        number.append(n)
        squared.append(n**2)
        cubed.append(n**3)
    data = [names] + list(zip(number, squared, cubed))
    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(12) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))

    keep_going = input("Would you like to continue (y?) - ")
    if keep_going.lower() != 'y':
        print("End!")
        break
    else:  
        print("\n Continue! \n")
        continue
print("")
    


# ### Convert given number grades into letter grades.
# 
# * Prompt the user for a numerical grade from 0 to 100.
# * Display the corresponding letter grade.
# * Prompt the user to continue.
# * Assume that the user will enter valid integers for the grades.
# * The application should only continue if the user agrees to.
# * Grade Ranges:
#   1. A : 100 - 88
#   2. B : 87 - 80
#   3. C : 79 - 67
#   4. D : 66 - 60
#   5. F : 59 - 0

# In[193]:


# Create a function that evaluates if a given value can convert to a float or not. 
# This allows grades float decimal grades to be evaluated
def isfloat(somevalue):
    try:
        float(somevalue)
        return True
    except ValueError:
        return False
    
# Contain the entire function in a while True loop to allow for repeat evaluations 
while True:

# create inner while True loop in order to evalaute whether a given input meets the requirements    
    while True:
        grade_percentage = input("What percentage did the student get. You can use decimal percentages! - ")
        if isfloat(grade_percentage) == True and float(grade_percentage) >= 0 and float(grade_percentage) <= 100:
            grade_percentage = float(grade_percentage)
            break
# Assign each percentage break down to a letter grade
    if grade_percentage <= 100 and grade_percentage >= 97:
        grade = 'A+'
    elif grade_percentage < 97 and grade_percentage >= 93:
        grade = 'A'
    elif grade_percentage < 93 and grade_percentage >= 90:
        grade = 'A-'
    elif grade_percentage < 90 and grade_percentage >= 87:
        grade = 'B+'
    elif grade_percentage < 87 and grade_percentage >= 83:
        grade = 'B'
    elif grade_percentage < 83 and grade_percentage >= 80:
        grade = 'B-'
    elif grade_percentage < 80 and grade_percentage >= 77:
        grade = 'C+'
    elif grade_percentage < 77 and grade_percentage >= 73:
        grade = 'C'
    elif grade_percentage < 73 and grade_percentage >= 70:
        grade = 'C-'
    elif grade_percentage < 70 and grade_percentage >= 67:
        grade = 'D+'
    elif grade_percentage < 67 and grade_percentage >= 65:
        grade = 'D'
    else:
        grade = 'F'
   # Print result with an an if the student recieved any A grade 
    if grade_percentage >= 90:
        print(f"The student recieved an {grade}")
   
   # Else print with an a 
    if grade_percentage < 90:
        print(f"The student recieved a {grade}")
    
    print("The grading scale came from: \n https://pages.collegeboard.org/how-to-convert-gpa-4.0-scale")
    # Ask the user if they would like to keep doing evaluations
    while True:
        keep_going = input("Would you like to continue (y/n?) - ")
        if keep_going == 'n' or keep_going == 'y':
            break
        else:
            print("Invalid Input! Try Agin!!")
        # If they put in anything other than a y end program
    if keep_going.lower() == 'n':
        print("End!")
        break
    # Else continue
    else:  
        print("\n Continue! \n")
        continue
print("")

# ### 6
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys:
# - title
# - author
# - genre

# In[19]:


my_books = [{"title":"Freakonomics",
             "author":"Stephen J. Dubner and Steven Levitt",
            "genre": "Non-Fiction"},
            
            {"title":"Why Nations Fail",
             "author":"Daron Acemoglu and James A. Robinson",
             "genre":"Non-Fiction"
            },
            
            {"title":"On A Pale Horse",
             "author":"Piers Anthony",
             "genre":"Fantasy"
            }, 
            
            {"title":"The Apprentice Adept",
             "author":"Piers Anthony",
             "genre":"Fantasy"
            }, 
            
            {"title":"The Vampire Lestat",
             "author":"Ann Rice",
             "genre":"Horror"
            },
           
            {"title":"Sawn Song",
             "author":"Robert R. McCammon",
             "genre":"Horror"
            }, 
           
            {"title":"Furies of Calderon",
             "author":"Jim Butcher",
             "genre":"Fantasy"
            }, 
            
            {"title":"The Regulators",
             "author":"Richard Bachman, Stephen King",
             "genre":"Horror"
            },
           
            {"title":"On World Order",
             "author":"Henry Kissinger",
             "genre":"Non-Fiction"
            },  
           
            {"title":"A Breach in the Watershed",
             "author":"Douglas Niles",
             "genre":"Fantasy"}
           ]


# * Loop through the list and print out information about each book.

# In[163]:


for book in my_books:
    print(book)
my_genres = [book['genre'] for book in my_books]
my_genres = list(set(my_genres))


# * Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[191]:

try_again = ()
while True:
    if try_again == "n":
        try_again = ()
        break
    genre = input("Search my books. Pick a genre - ") 
    genre = genre.capitalize()
    if genre == 'Non-fiction':
        genre = genre.replace('f', 'F')
    if genre in my_genres:
        print("")
        break
    else:
        while True:
            try_again = input(f"I don't read {genre} books. Try again? (y/n?)- ")
            if try_again == 'y' or try_again == 'n':
                break
            else:
                print("Invalid entry!")

if try_again != 'n':
    for book in my_books:
        if genre in book["genre"]:
            print(book["title"])
else:
    print("\n You stopped searching my libary")


# In[ ]:




