from datetime import datetime


def ticket_buy(age, ammount):
    ticket_age = {
        "1": 14,
        "2": 16,
        "3": 18,
        "4": 12
    }
    print("You want {} x{}? (y/n)".format(age, ammount))


now = datetime.now()
current_time = now.strftime("%H:%M")

# main
print(f"Time: {current_time}\n"
      f"========================================\n"
      f"What tickets would you like to purchase?")

ticket_buy(input(), input())
