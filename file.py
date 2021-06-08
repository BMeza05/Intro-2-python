num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # boolean
string = 'Hello World' # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, but with a list of different objects 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration with a dictoonary that has composite data, because it has more than one type, including a boolean, string, and numbers
fruit = ('blueberry', 'strawberry', 'banana') # variable with a tuple of different fruits
print(type(fruit)) # function with a tuple
print(pizza_toppings[1]) # function with a list and a string
pizza_toppings.append('Mushrooms') # a list with a function that acts on something within the list of toppings, probably to call it
print(person['name']) # a function that puts out a persons name on screen, using the dictionary
person['name'] = 'George' # a variable being declared using the dictionary with the string of names
person['eye_color'] = 'blue' # a variable declared using the dictionary "eye color" and the string within the dictionary
print(fruit[2]) # a function calling on a tuple and a fruit within the tuple                                                        

if num1 > 45:
    print("It's greater") # a conditional if statement that shows num1 if it is greater than 45, with an else statement just in case the number isnt greatetr than 45
else:
    print("It's lower")

if len(string) < 5: # an if statement that prints out some text if the length of the string is less than 5, with another else if condition that is met when the length is greater than 15, and another condition if neither is met 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # a for loop that shows X on screen while it is in range of a set of integers, probably 1-5
    print(x)
for x in range(2,5): # a for loop that shows X on screen while it is between 2 and 5
    print(x)
for x in range(2,10,3): # a for loop that shows X on screen while it is 2, 10, or 3
    print(x)
x = 0
while(x < 5): # a while loop that shows X on screen while it is less than 5, and adding 1 to X until it is greater than or equal to 5
    print(x)
    x += 1

pizza_toppings.pop() # a function that call on the last item on the list of pizza toppings
pizza_toppings.pop(1) # a function that calls on the second item on the list of pizza toppings

print(person) # shows a person and their attributes (i.e name and eye color)
person.pop('eye_color') # a function that calls on the eye color of the person
print(person) # shows a person and their attributes

for topping in pizza_toppings: #a for loop that calls on the toppings in pizza toppings. also has conditions to be met, and if they are specific toppings, then the loop will either continue or break
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # a function that prints the word hello 10 times
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # A function that prints hello x number of times
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # a function that prints out the word hello 10 times,
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) # a function that prints out the word hello 10 times, but this function is repeated 4 times, so the word hello comes out 40 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)