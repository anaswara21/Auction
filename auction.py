from replit import clear
from auctin_art import logo

#to print the logo of the auction game
print(logo)

#create a empty dictionary to save the name as key and bid amount as value
auction={}

#create a function to find the big bid amount and also print the winner
def highest_amount(dict_auction):
    highscore=0
    winner=" "
    for key in dict_auction:
        price=dict_auction[key]
        if price>highscore:
            highscore=price
            winner=key
    print(f"The winner is {winner} and the bid amount is ${highscore}")




should_continue =False
while not should_continue:
    name= input("What is your name:")
    bid=int(input("Enter your bid amount :$"))
    auction[name]=bid
    value =input("if there is another person for auction type 'YES' or type 'No':").lower()
    if value=="no":
        should_continue=True
        highest_amount(auction)
    else:
        clear()


    







