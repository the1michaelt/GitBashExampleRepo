import math
import random
from typing import OrderedDict

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
    # experimental test the pairs
    count = 0
    pairs_counted = 0
    # print (hands_dealt)
    while count <= 5:
        if player_hand[0] == player_hand[count]:
            pairs_counted += 1
            print(pairs_counted)
        else:
            print(end="")
        count += 1
        
    return(player_hand)

hand_to_player = deal_hand(after_deck_was_shuffled)
## WORKING
#4. deal to four players

def deal_to_players(hand_to_player, after_deck_was_shuffled):
    count=1
    while count <=4:
        print(f'Player', count, deal_hand(after_deck_was_shuffled))
        count +=1
    
hands_dealt=deal_to_players(hand_to_player, after_deck_was_shuffled)


# def deal_to_players(hand_to_player, after_deck_was_shuffled):
#     count = 1
#     while count <= 4:
#         print(f'Player', count, deal_hand(after_deck_was_shuffled))
#     
#     count += 1

# hands_dealt = deal_to_players(hand_to_player, after_deck_was_shuffled)



# # # taken in part from: https://www.tutorialspoint.com/python-check-if-all-elements-in-a-list-are-same
# # #5. Determining pair counts
# def determine_player_pair_counts(hand_to_player):
# #     # Using all()method
# #     card_holdings= hands_dealt
# #     index_number_forward = 0
# #     total_pairs=0
#     # count=0
#     # pairs_counted = 0
#     # # print (hands_dealt)
#     # while count <= 5:
#     #     if hands_dealt[0] == hands_dealt[count]:
#     #         pairs_counted+=1
#     #         print(pairs_counted)
#     #     else:
#     #         print(end="")
#     #     count+=1 

# pairs_in_hand= determine_player_pair_counts(hand_to_player)
    
# # # # EXPERIMENTAL
#4.  deal to four players with pair count

# def deal_to_players(hand_to_player):
#         return deal_hand(after_deck_was_shuffled)
  
# hands_dealt= deal_to_players(hand_to_player)

# # taken in part from: https://www.tutorialspoint.com/python-check-if-all-elements-in-a-list-are-same
# #5. Determining pair counts
# def determine_player_pair_counts(hands_dealt):
#     # print (hands_dealt[0])
#     # print (hands_dealt)
#     # count=1
#     # while count <= 5:
#     #     if hands_dealt[0]==hands_dealt[count]:
#     #         print(hands_dealt[0])
#     #     else:
#     #         print('false')
#     # count+=1
#     # # Result from count matches with result from len()
#     # # total_pairs=0
#     # index_number_end = len(hands_dealt)-1
#     # index_number_forward = 0
#     # while True:
#     #     if 0<= index_number_forward <= 4:
#     #         result = hands_dealt.count(hands_dealt[index_number_forward]) == hands_dealt[index_number_end]
#     #         index_number_end -= 1     
#     #     if (result):
#     #         print("All the elements are Equal")
#     # index_number_forward +=1
#     # # else:
#     # #     print("Elements are not equal")
    
    
#     # # Using all()method
#     # print(hands_dealt)
#     # # card_holdings= hands_dealt
#     # index_number_forward = 0
#     # total_pairs=0
#     # while index_number_forward <= 4:
#     #     result = all(cards == deal_to_players[0] for cards in hands_dealt)
#     #     index_number_forward += 1
#     #     if (result):
#     #         total_pairs += 1
#     #     # else:
#     #     #     print(", ")

# pairs_in_hand= determine_player_pair_counts(hands_dealt)


# # def run_functions(pairs_in_hand, hands_dealt):
# #     count=1
# #     while count <=4:
# #         deal_to_players(hand_to_player, after_deck_was_shuffled)
# #         determine_player_pair_counts(hands_dealt)
# #         count += 1

# run_functions(pairs_in_hand,hands_dealt)
    

#     pair_count=0
#     pair_count +=1
    
#     index_number_forward=0
    
    
#     index_number_back=4
#     index_number_back-=1
#     # ten possible outcomes - index number combinations of five cards
#     # if any of these are equal, (pair) 0=1,0=2, 0=3,0-4, 1=2,1=3,1=4, 2=3, 2=4, 3=4
#     # 0 has four outcomes, start at 1; 1 has three outcomes, start at 2; 2 has two outcomes start at 3; 3 only outcome is with 4
#     while count <= index_number_back:
#         for index_number_forward 
#         next_card= after_deck_was_shuffled[index_number_forward]
        
#         index_number_forward += 1
#         in range(1, index_number_back, 1)

     
     
#     while index_count = 0 <= 4:
#         if index_count = after_deck_was_shuffled[index_count]=
#         if yes = pair_count += 1
#         else pair_count
    
#     index_count += 1

# count_the_counts= determine_player_pair_counts(hand_to_player, after_deck_was_shuffled)

# # def test(after_deck_was_shuffled):
# #     # result = True
# #     # Get the first element
# #     first_element = after_deck_was_shuffled[0]
# #     # Compares all the elements with the first element
#     for word in after_deck_was_shuffled: 
#     if first_element != word:
#         result = False
#         print("All elements are not equal")
#         break
#     else:
#         result = True
#     if result:
#         print("All elements are equal")

# test(after_deck_was_shuffled)


    ###
    

# def (after_deck_was_shuffled):
#     result = True
#     index_count=0 #begins index string
#     compared_index_count=4 #ends index string
#     while index_count <=4: #counts forward
#         element = after_deck_was_shuffled[index_count]
#     # Compares all the elements with the first element
#     for value in after_deck_was_shuffled:
#     if element != word:
#         result = False
#         #   print("All elements are not equal")
#         #   break
#     else:
#         result = True
#     if result:
#         pair_count += 1


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


# #2. Deal five random cards
# def deal_five(card_stack):
#     count=1
#     while count <= 5:
#         print(random.choice(card_stack), end=", ")
#         count +=1
# hand_of_five= deal_five(card_stack)
# print(hand_of_five)
   

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
