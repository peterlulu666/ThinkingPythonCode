WHEELSNEEDED = 2
FRAMESNEEDED = 1
LINKSNEEDED = 50


def main():
    wheels = int(input("How many wheels do you have? "))
    frames = int(input("How many frames do you have? "))
    links = int(input("How many links do you have? "))
    bikeFromWheels = wheels / WHEELSNEEDED
    bikeFromFrames = frames / FRAMESNEEDED
    bikeFromLinks = links / LINKSNEEDED
    numberOfBike = int(min(bikeFromWheels,
                           bikeFromFrames,
                           bikeFromLinks))
    print("ALL totalled up, " +
          "you've got " + str(numberOfBike) +
          " bikes coming \n" +
          "I'm keeping the Leftovers for myself")
    leftWheels = wheels - numberOfBike * WHEELSNEEDED
    leftWheels2 = wheels % WHEELSNEEDED
    print(leftWheels2)
    leftFrame = frames - numberOfBike * FRAMESNEEDED
    leftLinks = links - numberOfBike * LINKSNEEDED
    print("Leftovers: ")
    print(str(leftWheels) + " wheels ")
    print(str(leftFrame) + " frames ")
    print(str(leftLinks) + " links ")


main()
