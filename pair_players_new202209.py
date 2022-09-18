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

# 3. Deals five cards to four players (concurrent) 
def deal_to_player(shuffled_deck):
    player = 1
    while player <= 5:
        cards = 0
        deal_hand = []
        while cards < 5:
            deal_card = shuffled_deck.pop(0)
            deal_hand.append(deal_card)
            cards += 1
            # return deal_hand
        print(f'Player {player}:{deal_hand}\n')
        player += 1
        
deal_five_to_each= deal_to_player(shuffled_deck)

# 3. select hand of 5 cards
# def deal_five_cards(shuffled_deck):
#     i = 0
#     deal_hand = []
#     while i < 5:
#         deal_card = shuffled_deck.pop(0)
#         deal_hand.append(deal_card)
#         i += 1
#         return deal_hand

# hand_for_each = deal_five_cards(shuffled_deck)

