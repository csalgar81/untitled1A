from taxi_class import Taxi, SilverServiceTaxi


def main():
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("q) quit,  c) choose taxi,   d) drive")
    user_input = input(">>> ")


    while user_input != 'q':

        if user_input == 'c':
            print_taxis_available(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            print("Bill to date: ${:<.2f}".format(bill_to_date))
        elif user_input == 'd':
            distance = int(input("Drive how far ? "))
            taxis[chosen_taxi].drive(distance)
            trip_cost = taxis[chosen_taxi].get_fare()
            print ("Your {} trip cost you ${:<.2f}".format(taxis[chosen_taxi].name,trip_cost))
            bill_to_date += trip_cost
            print("Bill to date: ${:<.2f}".format(bill_to_date))

        print("q) quit,  c) choose taxi,   d) drive")
        user_input = input(">>> ")
    print("Taxis are now:")
    print_taxis_available(taxis)




def print_taxis_available(taxis):
    print("Taxis available:")
    for i, item in enumerate(taxis):
        print(i, " - ", item)


main()
