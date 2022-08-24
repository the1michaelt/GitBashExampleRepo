import math
import random
from typing import OrderedDict
#all functions self contained. no global variables.

# Card_suit =[]

# for count in Card_suit:
#     print(count)
    
# for element in range(0,len(),1):
#     print(element)
    

#pair players

#no global variables

# #deck of cards

# # list3.append(list2.pop(0))

# # append, merge two lists together alternating

# def test():
#     Card_suit=['spade','club','diamond','hearts']
#     face_values=['A','K','Q','J','2','3','4','5','6','7','8','9','10']
#     for element in Card_suit:
#             print(element)
#             for element2 in face_values:
#                 print(element2)
# test()

# def card_deck():
#     Card_suit = ['of spades', 'of clubs', 'of diamonds', 'of hearts']
#     face_values = ['Ace', 'King', 'Queen', 'Jack', '2', '3',
#                 '4', '5', '6', '7', '8', '9', '10']
#     for element in Card_suit:    
#         for element2 in face_values:
#             print(element2,element, end=", ")
# card_deck()

# 1. Feat: Card deck with face values
def card_deck():
    card_suit = ['of spades', 'of clubs', 'of diamonds', 'of hearts']
    face_values = ['Ace', 'King', 'Queen', 'Jack', '2', '3',
                   '4', '5', '6', '7', '8', '9', '10']
    deck=[]
    for count in card_suit:
        for card_value in face_values:
            deck.append(card_value)
    # print (deck)  #print requires parentheses; return does not
    # card_count= len(deck)
    # print(card_count, ' cards.')
    return deck

card_stack=card_deck()

#2. shuffles the deck
def shuffle_deck():
    shuffled=random.sample(card_stack, k=len(card_stack))
    # print(shuffled)
    # print(len(card_stack))
    return (shuffled)
after_deck_was_shuffled= shuffle_deck()


#3. dealing a hand of five cards

def deal_hand(after_deck_was_shuffled):
    player_hand=[]
    count=1
    while count <= 5:
        removed_name = (after_deck_was_shuffled.pop())
        player_hand.append(removed_name)
        count+=1
    # print(player_hand)
    return(player_hand)

hand_to_player = deal_hand(after_deck_was_shuffled)


#4. deal to four players

def deal_to_players(hand_to_player, after_deck_was_shuffled):
    count=1
    while count <=4:
        print(f'Player', count, deal_hand(after_deck_was_shuffled))
        count +=1
    
deal_to_players(hand_to_player, after_deck_was_shuffled)

#5. Determining pair counts
def determine_player_pair_counts(deal_to_players(hand_to_player, after_deck_was_shuffled)):
  
    pair_count=0
    index_count=0
    while index_count = 0 <= 4:
        if index_count = after_deck_was_shuffled[index_count]=
        if yes = pair_count += 1
        else pair_count
    
    index_count += 1

count_the_counts= determine_player_pair_counts(hand_to_player, after_deck_was_shuffled)

def test(after_deck_was_shuffled):
result = True
# Get the first element
first_element = after_deck_was_shuffled[0]
# Compares all the elements with the first element
for word in after_deck_was_shuffled: 
   if first_element != word:
      result = False
      print("All elements are not equal")
      break
   else:
      result = True
   if result:
      print("All elements are equal")

test(after_deck_was_shuffled)


    ###
    

# def (after_deck_was_shuffled):

# result = True
# index_count=0 #begins index string
# compared_index_count=4 #ends index string
# while index_count <=4: #counts forward
#     element = after_deck_was_shuffled[index_count]
# # Compares all the elements with the first element
# for value in after_deck_was_shuffled:
#    if element != word:
#       result = False
#     #   print("All elements are not equal")
#     #   break
#    else:
#       result = True
#    if result:
#       pair_count += 1

# while compared_index_count >=0: #counts backward to 0
# # Get the first element
# element = after_deck_was_shuffled[index_count]
# # Compares all the elements with the first element
# for value in after_deck_was_shuffled:
#    if element != word:
#       result = False
#     #   print("All elements are not equal")
#     #   break
#    else:
#       result = True
#    if result:
#       pair_count -= 1


# element = after_deck_was_shuffled[index_count]
# # Compares all the elements with the first element
# for value in after_deck_was_shuffled:
#    if element != word:
#       result = False
#     #   print("All elements are not equal")
#     #   break
#    else:
#       result = True
#    if result:
#       pair_count +=1


# pairs=[]
# insert here determine, player count
        
#     return (pairs_p1,pairs_p2,pairs_p3,pairs_p4)



#   deck = []
#    for count in card_suit:
#         for card_value in face_values:
#             deck.append(card_value)
#     print(deck)  # print requires parentheses; return does not
#     card_count = len(deck)
#     print(card_count, ' cards.')
#     return deck

# names_list.remove('mike')
# print(names_list)




#2. shuffle cards
# 
# each number is not reusable

#creates a numeric index for each card
# def card_number_count(card_stack):
#     range_end = (len(card_stack)-1)  # returns 51
#     deck_count=[]
#     # for count in card_suit:
#     count=0
#     while 0 <= range_end:
#         count = random.randint(0, range_end)
#         deck_count.append(count)
#         # count +=1
#     return deck_count

# card_number_index= card_number_count(card_stack)
# print(card_number_index, end=", ")


# # random number from 0-51 to pick a card from the deck
# 



# random_number.pop



# for count in range(0,range_end,1)



# #deal random
# def deal_cards(card_stack):
#     count=1
#     if count <=5:
#         print(random.choice(card_stack))
#     else:
#         print ('stop')
#     count+=1
# deal_cards(card_stack)


# i = 1
# while i < 6:
#   print(i)
#   i += 1

# #2. Deal five random cards
# def deal_five(card_stack):
#     count=1
#     while count <= 5:
#         print(random.choice(card_stack), end=", ")
#         count +=1
# hand_of_five= deal_five(card_stack)
# print(hand_of_five)
   

# # def player_count():
#     Players = ['P1', 'P2', 'P3', 'P4', 'P5']
#     for which_player in Players:
#         return(which_player)
# player_number= player_count()

# def Player_hand(player_number, hand_of_five):
#     print(player_number,", ", hand_of_five)

# hand_dealt_by_player= Player_hand(player_number, hand_of_five)


# #deal five cards?
# # def card_deal(card_deck):
# #     deal = []
# #     while True:
# #         if count <=5:
# #             deal.append(random.choice(card_deck))
# #             print (deal)
# #         count +=1

# # card_deal(card_deck)


# # def deal_five(card_deck):
# #     for element in Card_suit:
# #         for element2 in face_values:
# #             element3 = (f'{element2} {element}')
# #             deck.append(element3)
# #             # print(deck)
# r_num0_2 = (random.randrange(0, 2))
# print(f"Random number from 0 to 2: {r_num0_2}.")

#     count = 1
#     if count<= 5:
#         for element5 in card_deck:
#             random.choice(card_deck)
#             print(element5)

# deal_five(c)


# # Deck=[]
# # while True:
# # Deck.append(Card_suit.pop(0))
# # Deck.append(face_values.pop(0))

# list3 = []
# while True:
# list3.append(list1.pop(0))
# list3.append(list2.pop(0))


# #combine two strings

# #players


#random cards assigned to each of four players

# #how to play
# Deal 5 cards
# To 4 players

# #shuffle deck
# Random.choice()

# mylist = ["apple", "banana", "cherry"]

# print(random.choice(mylist))

# #rules of game
# How many pairs(card == card)?

# #declare winner
# Print(player number)

# #declare


# def x():
#     return


# x()

# for y in z:
#     print


# if b:
#     else:

# while a(True):
#     return
