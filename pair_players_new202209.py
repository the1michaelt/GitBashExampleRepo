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
            print(f'Player {player}:{deal_hand}\n')
            # return deal_hand
        # check.determine_if_pairs()
            # deal_hand = deal_five_to_each
            if len(deal_hand)== 5:
                check_card = 1
                while check_card <= 3:
                    for this_card in deal_hand:
                        pairs = deal_hand.count(this_card)
                        if pairs > 1:
                            print(f'Player {player}: the {this_card} is paired.\n')                                                      
                    check_card += 1
                    print(f'Player {player}: there are no more pairs.\n')
                    break
        player += 1
deal_five_to_each= deal_to_player(shuffled_deck)


        #    if len(deal_hand) == 5:
        #        check_card = 1
        #        while check_card <= 3:
        #            first_card = deal_hand[check_card]  # Get the first card
        #            for card in deal_hand:
        #                 count first_card != card:  # not true
        #                     print("There are no pairs.")
        #                 else:
        #                     print("There are pairs.")
        #             check_card += 1



# 4. checking for pairs
def determine_if_pairs():
    # hand = deal_five_to_each
    first_card = deal_hand[0]  # Get the first card
    # Compares all the elements with the first card
    for card in hand:
        if first_card != card:  # not true
            print("There are no pairs.")
            break
        else:
            print("There are pairs.")


hand_pairs = determine_if_pairs()



# # 3. Deals five cards to four players (concurrent) 
# def deal_to_player(shuffled_deck):
#     player = 1
#     while player <= 5:
#         cards = 0
#         deal_hand = []
#         while cards < 5:
#             deal_card = shuffled_deck.pop(0)
#             deal_hand.append(deal_card)
#             cards += 1
#             # return deal_hand
#         print(f'Player {player}:{deal_hand}\n')
#         check.determine_if_pairs()
#         player += 1
    
# # deal_five_to_each= deal_to_player(shuffled_deck)

# # 4. checking for pairs 
# def determine_if_pairs():
#     hand = deal_five_to_each
#     first_card = hand[0]  # Get the first card
#     # Compares all the elements with the first card
#     for card in hand:
#         if first_card != card: #not true
#             print("There are no pairs.")
#             break
#         else:
#             print("There are pairs.")

# hand_pairs = determine_if_pairs()


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

