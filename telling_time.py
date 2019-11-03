import Time


def main():
    time = Time.Time()
    print("24-hour format ")
    time.set_format(24)
    print(time)
    print("12-hour format ")
    time.set_format(12)
    print(time)
    print("13 hour, 26 minute, 5 second")
    time.set_time(5, 26, 13)
    time.set_format(24)
    print(time)
    time.set_format(12)
    print(time)
    print("25 hour, 3 minute, 0 second")
    time.set_time(0, 3, 25)
    time.set_format(24)
    print(time)
    time.set_format(12)
    print(time)


main()
