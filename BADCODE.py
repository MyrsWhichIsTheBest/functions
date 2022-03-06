import sys
import time as t
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")
hours = int(now.strftime("%H"))
minutes = int(now.strftime("%M"))

timeslot1 = 0
timeslot2 = 0
timeslot3 = 0
movie_selection = 69
ticket_sold = 0
age_restrict = 0
ticket_type = 0
tickets_chosen = {

}


def movie_tickets():
    global movie_selection, ticket_sold
    print(f"{current_time}\n"
          f"Select Movie\n"
          f"===================================\n"
          f"(1) Free Guy (PG-13)\n"
          f"(2) Ma (R-16)\n")
    movie_selection = input()
    if movie_selection == "enddayearly":
        endday = input("End Day? (y/n)")
        if endday == "y":
            print(f"{ticket_sold} tickets sold.")
            print("Ending day...")
            t.sleep(1)
            sys.exit()
        else:
            movie_tickets()
    else:
        return movie_selection


def movie_selector():
    global movie_selection, age_restrict
    if movie_selection == "1":
        print(f"Free Guy (PG-13)\n"
              f"Available times:\n"
              f"(1) 10:30\n"
              f"(2) 13:15\n"
              f"(3) 17:55\n"
              f"(4) 22:10\n")
        time_chosen = input()
        age_restrict = 13
    elif movie_selection == "2":
        print(f"Ma (R-16)\n"
              f"Available times:\n"
              f"(1) 11:20\n"
              f"(2) 14:15\n"
              f"(3) 17:30\n"
              f"(4) 23:15\n")
        time_chosen = input()
        age_restrict = 16
    else:
        print("Error: Movie not available.")


def ticket_vendor():
    global ticket_type, tickets_chosen

    while ticket_type == 0:
        price = {
            "1": 15,
            "2": 18,
            "3": 20,
            "4": 10
            }
        selecting = 0
        while selecting == 0:
            print("Choose tickets: \n"
                  "(1) Child (under 8)"
                  "(2) Student (under 19)"
                  "(3) Adult"
                  "(4) Senior (70 and over)")
            ticket_type = input()
            amount = input("Amount of tickets?")
            print(f"{price[ticket_type]} x{amount}")
            tickets_chosen.update({price[ticket_type]: amount})
            print("More tickets? (y/n)")
            if input() == "n":
                break



movie_tickets()
movie_selector()
ticket_vendor()
