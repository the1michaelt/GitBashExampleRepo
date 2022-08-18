destinations = ['Museum Mile', 'Central Park','Little Korea', 'Times Square', 'Central Park']
restaurants = ["Junior's", "Jolibee's", "iTruli", "Bubba Gump", "Woorijip"]
transportation = ['a bus', 'a bike', 'an Uber ride', 'an e-scooter', 'a subway trip']
entertainment = ['tickets to the theater', 'drinks at an adult lounge', 'show at a comedy club', 'taping at a live show', 'tickets for a baseball game']

from operator import truediv
from optparse import Values
import random
from turtle import end_fill

# random choice values
def get_random_choice(list_of_options):
    first_random_choice = random.choice(list_of_options)
    return first_random_choice

# assigns value from the function to a variable
initial_destination = get_random_choice(destinations)
initial_restaurant = get_random_choice(restaurants)
initial_transportation = get_random_choice(transportation)
initial_entertainment = get_random_choice(entertainment)

#confirm user approval
def confirm_selection(list_of_options):
    while True:
        initial_choice = get_random_choice(list_of_options)
        print(initial_choice)
        user_response = input('Do you like this choice (y/n)? ')
        if user_response =='y':
            print(f'{initial_choice} is a great choice.')
            return initial_choice

selected_destination = confirm_selection(destinations)
selected_restaurant = confirm_selection(restaurants)
selected_transportation = confirm_selection(transportation)
selected_entertainment = confirm_selection(entertainment)

print(f'{selected_destination} in NYC is our recommended destination. You may eat at {selected_restaurant}, commute via {selected_transportation}, and enjoy {selected_entertainment}. Enjoy your visit.')