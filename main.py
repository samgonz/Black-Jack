import random
import splashScreen

deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_hand = []
users_hand = []
end_of_game = False
game_over = False

#Splash Screen
print(splashScreen.logo)

#Get the initial Startup hand
users_hand.append(random.choice(deck_of_cards))
users_hand.append(random.choice(deck_of_cards))
dealer_hand.append(random.choice(deck_of_cards))

#print the hands on the screen
print(f'Your hand is {users_hand}.')
print(f'Dealers hand is {dealer_hand}')

#Give Dealer their second card
dealer_hand.append(random.choice(deck_of_cards))

if sum(dealer_hand) == 21:
    """If dealers hand is 21, they hit black jack.
    End game flag is equal to True
    """    
    print('Dealer has Blackjack!\nYou lose!')
    game_over = True

if sum(users_hand) == 21:
    """If user hand is 21, they hit black jack.
    End game flag is equal to True
    """    
    print('You have Black Jack!\nYou Win!')
    game_over = True
    
if game_over == False:
    """If game isn't over, ask user if they would like to hit, fold or hold.
    """    
    continue_hand = input('Would you like to [hit], [hold] or [fold]?\n')
    print(f'Dealer second card a {deck_of_cards[-1]}.\n')
    print(f'Dealers hand is {dealer_hand}')

while game_over == False:
    """While game over is false, continue asking user if they would like to hit, hold or fold.
    """    
    if continue_hand.lower() == 'fold':     
        """if user selects fold, end the game.
        """           
        game_over == True
        print(f'Game Over, you folded with {sum(users_hand)}.\n')
        break
    
    if continue_hand.lower() == 'hold':
        """If user selects hold, stop asking user for cards.
        """        
        print(f'You have selected hold.\nYour score is {sum(users_hand)}.\n')
        break
    
    """If user selects hit, give user another card.
    """    
    users_hand.append(random.choice(deck_of_cards))
    print(f'You hit with a {users_hand[-1]}.\n')
    print(f'You total {sum(users_hand)}, Your hand is now {users_hand}.\n')
    
    if sum(users_hand) > 21:
        """If user hits and they get over 21, end the game.
        """        
        game_over == True
        print(f'Game Over, you busted with {sum(users_hand)}.\n')
        break
    
    continue_hand = input('Would you like to [hit], [hold] or [fold]?\n')
    
while sum(dealer_hand) < 17 and game_over == False:
    """If deals hand is under 17, force dealer to hit
    """    
    dealer_hand.append(random.choice(deck_of_cards))
    print(f'Dealer hits a {deck_of_cards[-1]}.\n')
    print(f'Dealer totals {sum(dealer_hand)}, their hand is now {dealer_hand}.\n')

if sum(dealer_hand) > 21 and game_over == False:
    """If dealer hits over 21, end game immediately
    """    
    print(f'You win! Dealer has busted with {sum(dealer_hand)}.\n')
    
if users_hand == dealer_hand and game_over == False:
    """If user and dealer has the same hand end the game.
    """    
    print(f'You tied!\n')
    
if users_hand > dealer_hand and game_over == False:
    """If user has a larger hand than dealer end game.
    """    
    print(f'You win! You have {sum(users_hand)} and dealer has {sum(dealer_hand)}.\n')

if dealer_hand > users_hand and game_over == False:
    """If dealer has a larger hand than user end game.
    """    
    print(f'You lose! You have {sum(users_hand)} and dealer has {sum(dealer_hand)}.\n')