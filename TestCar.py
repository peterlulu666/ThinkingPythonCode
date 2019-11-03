import Car


def main():
    # Create my_car object
    my_car = Car.Car()
    my_car.add_feature('heated seats')

    # Create your_car object
    your_car = Car.Car('Hillman', 'Minx')
    your_car.year = 1957
    your_car.price = 2500.0
    your_car.add_feature('power steering')

    print("My car is... ", my_car)
    print("")
    print("your car is... ", your_car)

    if my_car == your_car:
        print('We have the same thing!')
    else:
        print('You drive yours, I\'ll drive mine.')


main()
