from replit import clear
from art import logo
# #HINT: You can call clear() to clear the output in the console.
print(logo)
bidder = {}


def check_highest_bid(bidding_data):
    highest_bid = 0
    winner = ""
    for key in bidding_data:
        bid_amount = int(bidding_data[key])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"They winner is {winner} and won with a bid of {highest_bid}")


is_continue = True
while is_continue:
    name = input("What is your name: ")
    bid = input("What is your bid:$")
    bidder[name] = bid
    more_bidders = input("Are there any other bidders? type 'yes' or 'no'")
    if more_bidders == "no":
        is_continue = False
        check_highest_bid(bidder)
    elif more_bidders == "yes":
        clear()
        # max_num = 0
        # for key in bidder:
        #   if bidder[key] > max_num:
        #     max_num = bidder[key]
        # print(max_num)
