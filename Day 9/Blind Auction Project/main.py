# TODO-1: Ask the user for input
from art import logo
print(logo)
bids = {}
should_continue = False
while not should_continue:
        username = (input("What is your name?"))
        price = int(input("Your bid: $"))
        bids[username]= price
        if input("Is there any other bidder? 'yes' or 'no'") == "no":
            should_continue = True
            top_bid = 0
            winner =""
            for bid in bids:
                if bids[username] > top_bid:
                    top_bid += bids[username]
                    winner = bid
                    print(f"{winner} wins with a bid of ${top_bid}")
        else:
            print("\n" * 100)


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary


