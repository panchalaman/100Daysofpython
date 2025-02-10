import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
        return random.choice(cards)
def blackjack(list1):
    if sum(list1) == 21:
        return True
def result(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum2 > sum1:
        if sum2 <= 21:
            return True
        else:
            return False
computer_cards = []
user_cards = []
ace = 11
computer_cards.append(deal_card())
computer_cards.append(deal_card())
user_cards.append(deal_card())
user_cards.append(deal_card())
total_computer = sum(computer_cards)
total_user = sum(user_cards)
if blackjack(computer_cards):
    print("Computer won! Blackjack")
if blackjack(user_cards):
    print("User won! Blackjack")
print(f"COMPUTER CARDS : [{computer_cards[0]}, ?]")
print(f"USER CARDS : {user_cards}, SUM = {total_user}")
should_continue = True
while should_continue:
    total_computer = sum(computer_cards)
    action = input("Do you want to draw a card or call? Type 'draw' or 'call'").lower()
    if action == "draw":
        user_cards.append(deal_card())
    total_user = sum(user_cards)
    if ace in user_cards:
        if sum(computer_cards)>21:
            ace = 1
    if blackjack(user_cards):
        print("User won! Blackjack")
    if ace in computer_cards:
        if sum(computer_cards)>21:
            ace = 1
    if not result(computer_cards, user_cards):
        print("Score above 21, USER LOST!")
        should_continue = False
    if action == "call":
        if result(computer_cards, user_cards):
            print(f"\nCOMPUTER CARDS: {computer_cards} COMPUTER SCORE: {total_computer} \n USER WON!,")
        elif sum(computer_cards) > sum(user_cards):
            print(f"\nCOMPUTER CARDS: {computer_cards} COMPUTER SCORE: {total_computer} \n COMPUTER WON!,")
            should_continue = False
    print("\n" * 20)
    print(f"COMPUTER CARDS : [{computer_cards[0]}, ?]")
    print(f"USER CARDS : {user_cards}, SUM = {total_user}")
