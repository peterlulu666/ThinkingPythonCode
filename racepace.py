def main():
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    # Prompt the user for the number of kilometers, hours, and minutes
    while True:
        # Number of kilometers they ran, a floating-point number
        while True:
            kilometers = input("How many kilometers did you run? \n")
            try:
                # The distance is a float and is always greater than zero
                kilometers = float(kilometers)
                if kilometers > 0:
                    break
                else:
                    print("Oops, that wasn't a positive number, please try again!")
            except ValueError:
                print("Oops, that wasn't a floating-point number, please try again!")
        # Number of hours, a whole number
        while True:
            hours = input("How many hours did it take you? \n")
            if not hours.isdigit():
                print("Oops, that wasn't a whole number, please try again!")
            else:
                hours = int(hours)
                break
        # Number of minutes, a whole number
        while True:
            minutes = input("How many minutes? \n")
            if not minutes.isdigit():
                print("Oops, that wasn't a whole number, please try again!")
            else:
                minutes = int(minutes)
                break
        # Hours and minutes are both whole numbers,and either one may be zero, but the ​total​ time is never zero
        if hours == 0 and minutes == 0:
            print("The ​total​ time can not be zero \n")
            continue
        else:
            break
    # Compute the total number of miles ran, rounded off to two decimal places
    miles = round(0.621371 * kilometers, 2)
    # Compute the minutes and seconds pace-per-mile (​head’s up!!!​ If you do some calculation and
    # end up with, say, 10.8 minutes, that does ​not​ mean 10 minutes and 80 seconds... it means 10
    # minutes and 8/10 of a minute. You need to make that conversion into minutes and seconds.)
    seconds = hours * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE
    seconds_per_mile = seconds / miles
    minutes_per_mile = round(seconds_per_mile // SECONDS_PER_MINUTE)
    seconds_left_over = round(seconds_per_mile % SECONDS_PER_MINUTE)
    hours = seconds / SECONDS_PER_HOUR
    # Compute the average miles per hour, rounded off to two decimal places
    miles_per_hour = round(miles / hours, 2)
    # Report all of this information to the user
    print("You ran " + str(miles) + " miles ")
    print("Your pace: " + str(minutes_per_mile) + " min " + str(seconds_left_over) + " sec per mile ")
    print("Your MPH: " + str(miles_per_hour))


main()
