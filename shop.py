'''
Answer for Question 6 - PIAT: The Cheese Shop

Name: Jeslyn Joylie Bowman
SID: 530481526
unikey: jbow2146

'''

def buy_cheese(gold: int) -> tuple:
    while True:
        print("You have", gold, "gold to spend.")
        cheese_quantity = input("State [cheese quantity]: ").lower().split()
        if len(cheese_quantity) != 2 or cheese_quantity[0] != 'cheddar':
            if cheese_quantity == ['back']:
                return 0, 0
            else:
                print("Sorry, did not understand.")
                return 0, 0
        else:
            cheese = cheese_quantity[0]
            try:
                quantity = int(cheese_quantity[1])
            except (IndexError, ValueError):
                return None
            quantity = int(cheese_quantity[1])
            if quantity <=0:
                print("Must purchase a positive amount of cheese.")
                return 0, 0
            if gold < quantity*10:
                print("Insufficient gold.")
                return 0, 0
            else:
                gold_spent = quantity*10
                gold -= gold_spent
                print("Successfully purchase", quantity, "cheddar.")
                return gold_spent, quantity
        return None

def display_inventory(gold: int, cheese: int, trap: str) -> None:
    print("Gold -", gold)
    print("Cheddar -", cheese)
    print("Trap -", trap)

trap = ('High Strain Steel Trap', 'Hot Tub Trap', 'Cardboard and Hook Trap')

def main():
    import q4
    print("Welcome to The Cheese Shop!")
    print("Cheddar - 10 gold")
    gold = 125
    cheese = 0
    result = None
    while True:
        print("\nHow can I help ye?")
        print("1. Buy cheese\n2. View inventory\n3. Leave shop")
        activity = input()
        if activity == '1':
            gold_spent, cheese_bought = buy_cheese(gold)
            if cheese_bought == 0:
                continue
            gold -= gold_spent
            cheese += cheese_bought
        elif activity == '2':
            if q4.setup_trap == 'left':
                result = trap[0]
            elif q4.setup_trap == 'right':
                result = trap[1]
            else:
                result = trap[2]
            display_inventory(gold, cheese, result)
        elif activity == '3':
            break

if __name__ == '__main__':
    main()