print("Correctly identify the data types from the exercise")
print([99.9, "False", False, '0', 0, True, 'True', [{}], {'a': []}])
print("1 is a float -", type(99.9) == float)
print("2 is a str -", type("False") == str)
print("3 is a bool -", type(False) == bool)
print("4 is a str -", type('0') == str)
print("5 is a int - ", type(0) == int)
print("6 is a bool - ", type(True) == bool)
print("7 is a str -", type('True') == str)
print("8 is a list -", type([{}]) == list) 
print("9 is a dict -", type({'a': []}) == dict)
print("")

print("What data type would best represent:")
print("Q1: A term or phrase typed into a search box?") 
print("A1: A a list of a strings")
print("Q2: If a user is logged in?")
print("A2: A bool")
print("Q3: A discount amount to apply to a user's shopping cart?")
print("A3: A float")
print("Q4: Whether or not a coupon code is valid?")
print("A4: A bool")
print("Q5: An email address typed into a registration form?")
print("A5: A string")
print("Q6: The price of a product?")
print("A6: A float if it doesn't include a currency sign, a string if it does")
print("Q7: A Matrix?")
print("A7: A Dictionary")
print("Q8: The email addresses collected from a registration form?")
print("A8: A List")
print("Q9: Information about applicants to Codeup's data science program?")
print("A9: A Dictionary")
print("End"
"\n")

print("Predict what the result of evaluating it would be"
"\n" "Then execute the expression in your Python REPL.")
print("")
print("'1' + 2 will return an error")
print("6 % 4 will return 2")
print("type(6 % 4) will return int")
print("type(type(6 % 4)) will return type")
print("'3 + 4 is ' + 3 + 4 will return an error")
print("0 < 0 will return False")
print("'False' == False will return False") 
print("True == 'True' will return False")
print("5 >= -5 will return True")
print("!False or False will return nothing")
print("True or ""42"" will return True")  
print("!True && !False will return command not found error")
print("6 % 5 will return 1")
print("5 < 4 and 1 == 1 will return False")
print("'codeup' == 'codeup' and 'codeup' == 'Codeup' will return False")
print("4 >= 0 and 1 !== '1' will return an Error")
print("6 % 3 == 0 will return True")
print("5 % 2 != 0 will return True")
print("[1] + 2 will return an error can only concatanate lists")
print("[1] + [2] will return [1, 2]")
print("[1] * 2 will return [1, 1]")
print("[1] * [2] will return an error - can't multiply sequence by non-int of type 'list' ")
print("[] + [] == [] will return true")
print("{} + {} will return an error unsupported operand type(s) for +: 'dict' and 'dict'")
print("End"
"\n")

print("You have rented some movies for your kids: '\n' The little mermaid (for 3 days), '\n' Brother Bear (for 5 days, they love it), '\n' Hercules (1 day, you don't know yet if they're going to like it). '\n'If price for a movie per day is 3 dollars, how much will you have to pay?")
rented = [
    {'Movie':'The little mermaid',
            'Days': 3},
            {'Movie': 'Brother Bear',
            'Days': 5},
            {'Movie': 'Hercules',
            'Days': 1}
]
days = [x['Days'] for x in rented]  
print("The answer is", sum(days) * 3)
print("")

print("Suppose you're working as a contractor for 3 companies: '\n' Google, Amazon and Facebook, they pay you a different rate per hour. '\n' Google pays 400 dollars per hour, Amazon 380, and Facebook 350. '\n'How much will you receive in payment for this week? '\n' You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.")
work = [
    {'Company':'Google',
    'Pay':400,
    'Hours':6},
    {'Company':'Amazon',
    'Pay':380,
    'Hours':4},
    {'Company':'Facebook',
    'Pay':350,
    'Hours':10}     
]
pay_per_comp = [x['Pay'] * x['Hours'] for x in work]
print("The answer is", sum(pay_per_comp))

print("A student can be enrolled to a class only if  the class is '\n' not full and the class schedule does not conflict with her current schedule.")

class_not_full = True
student_conflict = False

def can_enroll(class_not_full, student_conflict):
    if class_not_full == True and student_conflict == False:
        return True
    return False
print(can_enroll(class_not_full, student_conflict),)
print("")

print("A product offer can be applied only if people buys more than 2 items, and the offer has not expired. '\n' Premium members do not need to buy a specific amount of products.")

import datetime
items_bought = 3
preimum_member = True
offer_valid = datetime.date(2020, 9, 8)

def can_apply_coupon(items_bought, preimum_member, offer_valid):
    if (items_bought > 2 or preimum_member == True) and offer_valid >= datetime.date.today():
        return True
    return False

print(can_apply_coupon(items_bought, preimum_member, offer_valid))
print("End")

print("Create a variable that holds a boolean value for each of the following")
print("username = 'codeup'")
print("password = 'notastrongpassword'")
print("the password must be at least 5 characters '\n' the username must be no more than 20 characters \n the password must not be the same as the username \n bonus neither the username or password can start or end with whitespace")
username = 'codeup'
password = 'notastrongpassword'

def is_valid(username, password):
    if len(username) >= 5 and len(username) <= 20  and username != password and username[0] != " " and password[0] != " ":
        return True
    return False
print(is_valid(username, password))