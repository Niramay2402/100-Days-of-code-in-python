# Would get the cards later on ... at the moment  just using random integers for the code
import random

bid = int(input("Enter the bid u want to put: "))


def check_winner(dealer, you):
    print(f"C:{dealer} Y:{you}")
    bank = 1000
    if you > 21:
        print("BUST")
        bank -= bid
        print(f"Your bank Balance: {bank}")
    elif dealer < you:
        print("You win")
        bank += bid
        print(f"Your bank Balance: {bank}")
    elif dealer == you:
        print("Push")
    else:
        print("You lost ")
        bank -= bid
        print(f"Your bank Balance: {bank}")


# def hit(y_cards):
#     your_cards = y_cards + random.randint(1, 11)
#
#     return f"{your_cards}"
#
#
# def stand(d_cards):
#     dealer_cards = d_cards + random.randint(1, 11)
#
#     return f"{dealer_cards}"


dealer_cards = random.randint(1, 11)
your_cards = random.randint(1, 21)

print(f"computer:{dealer_cards} \nyour card:{your_cards}")

dealer_cards += random.randint(1, 11)


print(f"\nC:{dealer_cards}")


def checking_condition(yCards):
    if yCards < 21:
        False
    elif yCards < 21:
        False


black = True

while black:
    wanna_play_more = input("Wanna hit or stand ?....Type h for hit or s for stand...")

    if wanna_play_more == 'h':
        your_cards += random.randint(1, 11)
        print(f"\n{your_cards}")
        checking_condition(yCards= your_cards)
    elif wanna_play_more == 's':
        dealer_cards += random.randint(1, 11)
        checking_condition(yCards= dealer_cards)
        check_winner(dealer_cards, your_cards)
    else:
        print("enter a valid input")


check_winner(dealer_cards, your_cards)
