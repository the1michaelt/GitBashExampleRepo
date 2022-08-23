import math
import random
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

# 1. Design card deck
def card_deck():
    card_suit = ['of spades', 'of clubs', 'of diamonds', 'of hearts']
    face_values = ['Ace', 'King', 'Queen', 'Jack', '2', '3',
                   '4', '5', '6', '7', '8', '9', '10']
    deck=[]
    for element2 in face_values:
        for element in card_suit:
            # element3 = f'{element2} {element}'
            deck.append(element)
            print(len(deck))
    return deck

card_stack=card_deck()

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
   

# def player_count():
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
# # r_num0_2 = (random.randrange(0, 2))
# # print(f"Random number from 0 to 2: {r_num0_2}.")

# #     count = 1
# #     if count<= 5:
# #         for element5 in card_deck:
# #             random.choice(card_deck)
# #             print(element5)

# # deal_five(c)


# # # Deck=[]
# # # while True:
# # # Deck.append(Card_suit.pop(0))
# # # Deck.append(face_values.pop(0))

# # list3 = []
# # while True:
# # list3.append(list1.pop(0))
# # list3.append(list2.pop(0))


# # #combine two strings

# # #players


# #random cards assigned to each of four players

# # #how to play
# # Deal 5 cards
# # To 4 players

# # #shuffle deck
# # Random.choice()

# # mylist = ["apple", "banana", "cherry"]

# # print(random.choice(mylist))

# # #rules of game
# # How many pairs(card == card)?

# # #declare winner
# # Print(player number)

# # #declare


# # def x():
# #     return


# # x()

# # for y in z:
# #     print


# # if b:
# #     else:

# # while a(True):
# #     return
