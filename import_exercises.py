# 1) Test the import functionality by importing time module and running a fuctions from it
import time

# This the sleep function causes the script to wait x number of seconds defore moving onto the next task
time.sleep(2)
print('All Done!')

# 2) Import time using the alias tim to test the function
import time as tim
tim.sleep(5)
print("That was a long time!")

# 3) Import a single function from the time module
from time import gmtime
gmtime()

# 4) Import gmtime using an alias
from time import gmtime as gm
gm()


# 5) Ansewring the following questions using functions within the intertools module
import itertools as iter
# Get how many pairs of 'ABC' and '123' there be
ABC123 = list(iter.product(['A', 'B', 'C'], ['1', '2', '3']))
# Get how many pairs of abcd there can be
pairs_abcd = list(iter.combinations('abcd', 2))
# Get how many different combinations of 'abcd' there can be
two_combo_abcd = list(iter.permutations('abdc', 2))
# use len to answer how many results there are
print(len(ABC123))
print(len(pairs_abcd))
print(len(two_combo_abcd))

# 6) Import the json module and use it to read the data file profiles.json into a list of dictionaries
import json
with open('/Users/anthonystraine/codeup-data-science/python-exercises/profiles.json') as f:
    # assian it to object called profiles
    profiles = json.load(f)

# 7) Find the number of users
users = [profile.get("_id") for profile in profiles]
print(len(users))

# 8) Find the number of active users
# use list comprehension to extract the True or False values for each user
is_active = [profile['isActive'] for profile in profiles]
# then use count(True) to find how many active users there are
print(is_active.count(True))

# 9) Find the number of inActive users
# use the isActive list to count how many False values there are
print(is_active.count(False))

# 10) Find the grand total of balances for all users

# use list comprehension to interate over the the list of dictionaries to
# get the balance of each user
total_balance = [profile['balance'] for profile in profiles]
# then use list comprehension again to strip out $ and commas and then convert to float
total_balance = sum([float(total.replace('$', "").replace(",", "")) for total in total_balance])
print('$' + str(total_balance))

# 11) Find the average balace per user
avg_balance = total_balance/len(users)
print(f"$ + {avg_balance}")

# 12) User with the lowerst balance 
# 13) User with the lowerst balance 
low_user_id = ""
lowest_balance = 1000000000000000000000000
for profile in profiles:
    user_balance = float(profile['balance'].replace('$', '').replace(',', ''))
    if user_balance < lowest_balance:
        low_user_id = profile['_id']
        lowest_balance = user_balance

print(f"User with the lowest balance is ID: {low_user_id}")    

# 13) User with the highest balance 
high_user_id = ""
top_balance = 0
for profile in profiles:
    user_balance = float(profile['balance'].replace('$', '').replace(',', ''))
    if user_balance > top_balance:
        high_user_id = profile['_id']
        top_balance = user_balance
        
print(f"User with the maximum balance is ID: {high_user_id}")   

# 14) What is the most commmon favorite fruit?
# use list comprehension to assign the list of fruits from the dictionary to variable fruits
fruits = [profile['favoriteFruit'] for profile in profiles]

# create empty values for top_fruit and make top_count default 0 to use as reference points
top_fruit = ''
top_count = 0
# iterate over the values in fruits
for fruit in fruits:
    # if count of fruit is greater than the top count
    if fruits.count(fruit) > top_count:
        # assign fruit to the top fruit value
        top_fruit = fruit
        # and assign the new count to top_count
        top_count = fruits.count(fruit)

print(top_fruit)

# 15) Which is the least common favorite fruit
lower_fav_fruit = ''
low_count = 1000000000000000000
for fruit in fruits:
    if fruits.count(fruit) < low_count:
        lower_fav_fruit = fruit
        low_count = fruits.count(fruit)

print(lower_fav_fruit)

# 16) Find the total number of unread messages across all users
# Use list comprehension to create a list of all greetings from profiles
greetings = [profile['greeting'] for profile in profiles]

# create an empty string to store the number of every message
messages = []

#Use a for loop to get inside each string in the list of greetings
for greeting in greetings:
    # Looking at the data, we know each greetings message has only 1 ! that appears after the user's full name followed by a sapce. 
    # We can use the ! to get the index value we want to slice off add 1 to it to account for the space after the !
    # Reassign greeting to that new value
    greeting = greeting[greeting.index('!') + 1:]
    # After getting rid of the begining of the greeting, we can replace "You have " and " uread message." - 
    # with nothing to leave only the number of messages and then reassign that to greeting
    greeting = greeting.replace("You have ", "").replace(" unread messages.", "")
    # Then append the value converted to an int to messages
    messages.append(int(greeting))

# Then print the sum of the messages list
print(f"The total number of unread messages across all users is {sum(messages)}")
