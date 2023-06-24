import random

deck = {
    'Ace of Spades': 1,
    '2 of Spades': 2,
    '3 of Spades': 3,
    '4 of Spades': 4,
    '5 of Spades': 5,
    '6 of Spades': 6,
    '7 of Spades': 7,
    '8 of Spades': 8,
    '9 of Spades': 9,
    '10 of Spades': 10,
    'Jack of Spades': 10,
    'Queen of Spades': 10,
    'King of Spades': 10,
    'Ace of Hearts': 1,
    '2 of Hearts': 2,
    '3 of Hearts': 3,
    '4 of Hearts': 4,
    '5 of Hearts': 5,
    '6 of Hearts': 6,
    '7 of Hearts': 7,
    '8 of Hearts': 8,
    '9 of Hearts': 9,
    '10 of Hearts': 10,
    'Jack of Hearts': 10,
    'Queen of Hearts': 10,
    'King of Hearts': 10,
    'Ace of Diamonds': 1,
    '2 of Diamonds': 2,
    '3 of Diamonds': 3,
    '4 of Diamonds': 4,
    '5 of Diamonds': 5,
    '6 of Diamonds': 6,
    '7 of Diamonds': 7,
    '8 of Diamonds': 8,
    '9 of Diamonds': 9,
    '10 of Diamonds': 10,
    'Jack of Diamonds': 10,
    'Queen of Diamonds': 10,
    'King of Diamonds': 10,
    'Ace of Clubs': 1,
    '2 of Clubs': 2,
    '3 of Clubs': 3,
    '4 of Clubs': 4,
    '5 of Clubs': 5,
    '6 of Clubs': 6,
    '7 of Clubs': 7,
    '8 of Clubs': 8,
    '9 of Clubs': 9,
    '10 of Clubs': 10,
    'Jack of Clubs': 10,
    'Queen of Clubs': 10,
    'King of Clubs': 10
}


def calculate_total(hand):
    total = sum(hand)
    if 1 in hand and total + 10 <= 21:
        total += 10
    return total


def blackjack():
    player_total = calculate_total(your_hand)
    dealer_total = calculate_total(dealer_hand)

    if player_total > 21:
        print("You bust! You lose.")
    elif player_total == 21 and dealer_total != 21:
        print("You have blackjack! You win.")
    elif player_total < 21 and dealer_total < 21 and player_total > dealer_total:
        print("Player wins!")
    elif player_total < 21 and dealer_total > 21:
        print("Dealer busts! Player wins.")
    elif player_total == dealer_total:
        print("It's a draw!")
    else:
        print("Dealer wins.")


game_start = input("Do you want to start the game? (yes/no): ")
your_hand = []
dealer_hand = []

if game_start.lower() != "yes":
    print("End of the program.")
else:
    your_hand.extend(random.choices(list(deck.values()), k=2))
    dealer_hand.extend(random.choices(list(deck.values()), k=2))

    print("Your hand:", your_hand)
    print("Dealer's hand:", [dealer_hand[0], "Hidden Card"])


    while True:
        player_choice = input("Do you want to hit or stand? (hit/stand): ")
        if player_choice.lower() == "hit":
            your_hand.append(random.choice(list(deck.values())))
            print("Your hand:", your_hand)

            if calculate_total(your_hand) > 21:
                print("You bust! You lose.")
                break
        elif player_choice.lower() == "stand":
            print("Player stands. Dealer's turn.")

            # Dealer's turn
            while calculate_total(dealer_hand) < 17:
                dealer_hand.append(random.choice(list(deck.values())))

            print("Dealer's hand:", dealer_hand)

            blackjack()  # Determine the winner
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")





