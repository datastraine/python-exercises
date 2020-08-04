# 1) Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(two):
    if two == 2 or two == '2':
        return True
    return False

print(is_two(input("Enter something. Is it two? - ")))
print("Next question ! \n")

# 2) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    return False

print(is_vowel(input("Enter a letter. Is it a vowel? - ")))
print("Next question ! \n")

# 3) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(letter):
    if is_vowel(letter.lower()):
        return False
    return True

print(is_consonant(input("Enter a letter. Is it a consonant? - ")))

# 4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_first_letter(word):
    if is_consonant(word[:1]) == True:
        return word.capitalize()
    return word

print(capitalize_first_letter(input("Enter a word. If it starts with a consonant, it will capitalize it - ")))
print("Next question ! \n")

# 5) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# Pure function method
def calculate_tip1(bill, tip):
    tip_amount = float(tip) * float(bill)
    return (f"Your tip should be {'$' + str(tip_amount)}")

print(calculate_tip1(input("Enter the bill total. - "), input("Enter the percentage you wish to tip")))


# Method while forcing user inputs to be in proper format without requiring a given statment
def calculate_tip2():
    while True: 
        bill = input("How much is your bill? - ")
        if type(float(bill)) ==  float:
            bill = float(bill)
            break
    
    while True:
        tip = input("What percentage of the bill do you want to leave as a tip? - ")
        if type(float(tip)) ==  float and float(tip) >= 0 and float(tip) <= 1:
            tip = float(tip)
            break
    
    tip_amount = tip * bill
    return (f"Your tip should be {'$' + str(tip_amount)}")

print(calculate_tip2())

def apply_discount(original_price, discount):
    assert type(original_price) != str, 'Original Price must be in float or int format'
    assert type(discount) != str and discount >= 0 and discount <= 1, 'Discount must be a float between 0 and 1'

    new_price = str(original_price - (original_price * discount))
    print(f"The new price of your item is {'$' + new_price}")
    
apply_discount(500, .33)

# 6) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output
def handle_commas(x):
    while x.find(',') > 0:
        somevalue = x.replace(",", "")
        try:
            type(int(somevalue)) == int
            print(somevalue)
            break
        except:
            try:
                if type(float(somevalue)) == float:
                    print(somevalue)
            except:
                print(f"{x} is not a number")
        break
    else:
        print(f"{x} does not have a comma") 
print("Enter a value to check for commas see if the value can be translated to a number, stip the common")
handle_commas(100,000)

# 7) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number):
    #assert type(number) == int or type(number) == float, 'Argument must be either a int or a float'
    if number <= 100 and number >= 97:
        grade = 'A+'
    elif number < 97 and number >= 93:
        grade = 'A'
    elif number < 93 and number >= 90:
        grade = 'A-'
    elif number < 90 and number >= 87:
        grade = 'B+'
    elif number < 87 and number >= 83:
        grade = 'B'
    elif number < 83 and number >= 80:
        grade = 'B-'
    elif number < 80 and number >= 77:
        grade = 'C+'
    elif number < 77 and number >= 73:
        grade = 'C'
    elif number < 73 and number >= 70:
        grade = 'C-'
    elif number < 70 and number >= 67:
        grade = 'D+'
    elif number < 67 and number >= 65:
        grade = 'D'
    else:
        grade = 'F'
   # Print result with an an if the student recieved any A grade 
    if number >= 90:
        print(f"The student recieved an {grade}")
   # Else print with an a 
    else:
        print(f"The student recieved a {grade}")

assert get_letter_grade(100) == 'A+'

