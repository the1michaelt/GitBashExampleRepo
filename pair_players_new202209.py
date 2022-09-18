import random

#1. create 52 cards
def create_cards():
    values= ['Ace','King','Queen','Jack','2','3','4','5','6','7','8','9','10']
    i = 0
    while i < 2:  #needs two iterations
        values += values  #doubles the card face values per iteration
        i += 1  
    return values
create_deck= create_cards()

#2. shuffle deck
def randomize_cards(create_deck, random):
    mixed_deck = random.sample(create_deck, k=len(create_deck)) #k=len (length of card deck is necessary as the second argument)
    return mixed_deck

shuffled_deck= randomize_cards(create_deck, random)

#3. select hand of 5 cards
def deal_hand_to_players(shuffled_deck):
    i = 0
    deal_hand = []
    while i < 5:
        deal_card = shuffled_deck.pop()
        deal_hand.append(deal_card)
        i += 1
        return deal_hand
 
hand_for_each = deal_hand_to_players(shuffled_deck)

#4. 


# #3. deal hand of 5 cards to four players
# def deal_hand_to_players(shuffled_deck, random):
#     i = 0
#     while i < 3:  # deals 4 times
#         while i < 4:
#             deal_deck = []
#             deal_deck += shuffled_deck
#             i += 1
#             print(deal_deck)
#         i += 1


# deal_hand = deal_hand_to_players(shuffled_deck, random)



#4. 