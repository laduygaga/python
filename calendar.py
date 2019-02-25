from time import sleep, strftime

USER_FIRST_NAME = "DUY"

calendar = {}


def welcome():
    print("Welcome " + USER_FIRST_NAME + ".")
    print("Calendar openned")
    sleep(1)
    print("Today is: " + strftime("%A %B %d %Y"))
    print("Current time is: " + strftime("%H %M %S"))
    print("What would you like to do")


def start_calendar():
    welcome()
    start = True
    while start is True:
        user_choice = input("Enter A to Add, V to view, \
D to Delete, X to Exit: ").upper()
        if user_choice == "V":
            if len(calendar) < 1:
                print("calendar is empty.")
            else:
                print(calendar)

        elif user_choice == "A":
            date = input("Enter date (MM/DD/YYYY): ")
            event = input("Enter event: ")
            calendar[date] = event
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("A date format MM/DD/YYYY")
                print("Year is invalid.")
                try_again = input("Try again? Y for Yes, N for No: ").upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                print(calendar)

        elif user_choice == "D":
            if len(calendar) < 1:
                print("Calendar is empty")
            else:
                event = input("What is even?")
                for date in calendar:
                    if calendar[date] == event:
                        del calendar[date]
                        print("Event was successfully deleted")
                        break
                    else:
                        print("Incorrect event")

        elif user_choice == "X":
            start = False

        else:
            print("Invalid command!")
            start = False


start_calendar()
