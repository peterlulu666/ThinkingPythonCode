def main():
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60
    # Prompt the user for the number of kilometers, hours, and minutes
    # Number of kilometers they ran, a floating-point number
    while True:
        # make sure that the user has provided an integer, not a float or a string or anything else
        # isdigit() checks whether the string consists of digits only
        try:
            kilometers = float(input("How many kilometers did you run? \n"))
            if kilometers >= 0:
                break
            else:
                print("Oops, that wasn't a positive number, please try again!")
        except ValueError:
            print("Oops, that wasn't a floating-point number, please try again!")
    # Number of hours, a whole number
    hours = input("How many hours did it take you? \n")
    while True:
        # make sure that the user has provided an integer, not a float or a string or anything else
        # isdigit() checks whether the string consists of digits only
        if not hours.isdigit():
            print("Oops, that wasn't a whole number, please try again!")
        else:
            hours = int(hours)
            break
        hours = input("How many hours did it take you? \n")
    # Number of minutes, a whole number
    minutes = input("How many minutes? \n")
    while True:
        # make sure that the user has provided an integer, not a float or a string or anything else
        # isdigit() checks whether the string consists of digits only
        if not minutes.isdigit():
            print("Oops, that wasn't a whole number, please try again!")
        else:
            minutes = int(minutes)
            break
        minutes = input("How many minutes? \n")
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